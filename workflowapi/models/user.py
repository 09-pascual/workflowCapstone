from django.db import models


class User(models.Model):
    
    ROLE_CHOICES = [
        ('Admin', 'Admin'),
        ('Manager', 'Manager'),
        ('Worker', 'Worker'),
        ('Customer', 'Customer')
    ]
   
    user_name = models.CharField(max_length=200)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    birthdate = models.DateField()
    phone_number= models.CharField(max_length=15)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)
    
    def __str__(self):
        return self.user_name
