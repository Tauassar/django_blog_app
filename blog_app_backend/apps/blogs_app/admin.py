from django.contrib import admin

from apps.blogs_app.models import BlogEntity, ReadBlogs

admin.site.register(BlogEntity)
admin.site.register(ReadBlogs)
