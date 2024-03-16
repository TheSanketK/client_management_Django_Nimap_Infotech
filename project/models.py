# Create your models here.
from django.db import models
from client.models import Client  # Import the Client model from the client app
from user.models import User  # Import the User model from the user app

# class Project(models.Model):
#     name = models.CharField(max_length=100)
#     client = models.ForeignKey(Client, on_delete=models.CASCADE)  # Link to the Client model
#     users = models.ManyToManyField(User)  # Link to the User model
#     created_at = models.DateTimeField(auto_now_add=True)
#     created_by = models.ForeignKey(User, on_delete=models.CASCADE)  # Link to the User model
    
#     def __str__(self):
#         return self.name

from django.db import models
from user.models import User  # Assuming your User model is defined in 'user' app

class Project(models.Model):
    name = models.CharField(max_length=100)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_projects')
    users = models.ManyToManyField(User, related_name='assigned_projects')
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
