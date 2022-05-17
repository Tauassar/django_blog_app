import logging

from django.contrib.auth import get_user_model
from rest_framework.mixins import ListModelMixin, CreateModelMixin, DestroyModelMixin
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from rest_framework import status


from apps.users_app.serializers import FollowingSerializer
from blog_app_backend.celery import debug_task

logger = logging.getLogger(__name__)


class SubscriptionView(
    ListModelMixin,
    DestroyModelMixin,
    CreateModelMixin,
    GenericViewSet
):
    """
    View for deleting/creating/listing read books
    """
    queryset = get_user_model().objects.all()
    serializer_class = FollowingSerializer

    def get_queryset(self):
        queryset = self.queryset
        logger.debug(f'User {self.request.user} requested subscriptions view')
        return queryset.filter(id=self.request.user.id)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.request.user.following.add(serializer.data['following'][0])
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def destroy(self, request, *args, **kwargs):
        self.request.user.following.remove(kwargs.get('pk'))
        logger.info(f"Deleted subscription for user {request.user} on user with id {kwargs.get('pk')}")
        return Response(status=status.HTTP_204_NO_CONTENT)
