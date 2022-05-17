import logging

from rest_framework.decorators import action
from rest_framework.mixins import CreateModelMixin, DestroyModelMixin, RetrieveModelMixin, ListModelMixin
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, GenericViewSet

from apps.blogs_app.models import BlogEntity, ReadBlogs
from apps.blogs_app.paginators import BlogEntityPagination
from apps.blogs_app.serializers import BlogEntitySerializer, ReadBlogsSerializer
from apps.blogs_app.utils import get_read_blogs, get_following_users_list, get_feed_queryset
from blog_app_backend.celery import debug_task

logger = logging.getLogger(__name__)


class ReadBlogsView(
    ListModelMixin,
    DestroyModelMixin,
    RetrieveModelMixin,
    CreateModelMixin,
    GenericViewSet
):
    """
    View for deleting/creating/listing read books
    """
    queryset = ReadBlogs.objects.all()
    serializer_class = ReadBlogsSerializer

    def get_queryset(self):
        queryset = self.queryset
        logger.debug(f'User {self.request.user} requested read blogs view')
        query_set = queryset.filter(user=self.request.user)
        return query_set


class BlogView(ModelViewSet):
    """
    Viewset for reading/writing/deleting/editing blogs
    """
    queryset = BlogEntity.objects
    serializer_class = BlogEntitySerializer
    pagination_class = BlogEntityPagination

    def get_queryset(self):
        queryset = self.queryset
        request_user = self.request.user
        return queryset.filter(
            creator_id=request_user.id
        )

    @action(methods=["get"], detail=False, url_path="feed", url_name="blogs_feed")
    def list_feed_blogs(self, request, *args, **kwargs):
        queryset = get_feed_queryset(self.request.user)

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
