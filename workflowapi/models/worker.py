from django.db import models
from .user import User


class Worker(models.Model):
    
    AVAILABILITY_STATUS= [
        ('working', 'working'),
        ('off', 'off')
    ]
    
    user = models.OneToOneField(User, on_delete=models.DO_NOTHING)
    availability = models.CharField(max_length=200)
    