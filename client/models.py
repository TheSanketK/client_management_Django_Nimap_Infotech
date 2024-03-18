from django.db import models
from user.models import User  # Import the User model from the user app

class Client(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)  # Link to the User model
    
    def __str__(self):
        return self.name
