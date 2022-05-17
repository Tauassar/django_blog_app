from django.contrib import admin

from apps.users_app.models import CustomUser

admin.site.register(CustomUser)
