from django.db import models

from apps.users_app.models import CustomUser


class BlogEntity(models.Model):
    class Meta:
        db_table = 'blog_entities'

    creator = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        verbose_name="Created by",
        related_name='posts'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=40)
    body = models.TextField(max_length=140)


class ReadBlogs(models.Model):
    class Meta:
        db_table = 'read_blogs'

    user = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name='read_posts'
    )
    blog = models.ForeignKey(
        BlogEntity,
        on_delete=models.CASCADE,
        related_name='read_posts'
    )
    read_at = models.DateTimeField(auto_now_add=True)
