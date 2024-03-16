from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    email = models.EmailField(unique=True)
    # You might want to add other fields as per your requirements

    def __str__(self):
        return self.username

# Add related_name to avoid clash with auth.User.groups
User.groups.field.remote_field.related_name = 'custom_user_groups'

# Add related_name to avoid clash with auth.User.user_permissions
User.user_permissions.field.remote_field.related_name = 'custom_user_permissions'
