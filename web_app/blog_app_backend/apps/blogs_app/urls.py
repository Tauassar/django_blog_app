from django.urls import path, include
from rest_framework.routers import DefaultRouter

# Create a router and register our viewsets with it.
from apps.blogs_app.views import BlogView, ReadBlogsView

router = DefaultRouter()
router.register(r'', BlogView, basename="blogs")
router.register(r'read', ReadBlogsView, basename="read")

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
]
