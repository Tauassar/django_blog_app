from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    class Meta:
        db_table = 'users'

    following = models.ManyToManyField(
        "CustomUser", related_name="followings", blank=True,
    )

    def __str__(self):
        return f'{self.email} - {self.first_name} {self.last_name}'
