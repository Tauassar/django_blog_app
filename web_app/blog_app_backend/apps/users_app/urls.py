from django.urls import path, include
from rest_framework.routers import DefaultRouter

from apps.users_app.views import SubscriptionView

router = DefaultRouter()
router.register(r'subscription', SubscriptionView, basename="read")

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
]
