from apps.users_app.models import CustomUser
from rest_framework.serializers import ModelSerializer, PrimaryKeyRelatedField


class FollowingSerializer(ModelSerializer):
    following = PrimaryKeyRelatedField(
        many=True,
        queryset=CustomUser.objects.all()
    )

    class Meta:
        model = CustomUser
        fields = ['following']
