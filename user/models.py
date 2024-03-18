from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.username

User.groups.field.remote_field.related_name = 'custom_user_groups'

User.user_permissions.field.remote_field.related_name = 'custom_user_permissions'
