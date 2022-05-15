import logging

from rest_framework.serializers import ModelSerializer

from apps.blogs_app.models import ReadBlogs, BlogEntity

logger = logging.getLogger(__name__)


class ReadBlogsSerializer(ModelSerializer):
    class Meta:
        model = ReadBlogs
        fields = ['id', 'user', 'blog']

    def create(self, validated_data):
        user = self.context.get("request").user
        logger.debug(f'Creating read blog for {user}')
        return ReadBlogs.objects.create(
            user_id=user.id,
            **validated_data
        )


class BlogEntitySerializer(ModelSerializer):
    class Meta:
        model = BlogEntity
        fields = ['title', 'body']

    def create(self, validated_data):
        user = self.context.get("request").user
        logger.debug(f'Creating blog entity for user {user}')
        return BlogEntity.objects.create(
            **validated_data,
            creator=user
        )
