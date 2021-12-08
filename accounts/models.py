from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth import get_user_model

class CustomUser(AbstractUser):
    phonenumber = models.CharField(max_length=10, null=True, blank=True)
    
    def __str__(self):
        return self.email