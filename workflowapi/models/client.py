from django.db import models


class Client(models.Model):
    first_name= models.CharField(max_length=200)
    last_name= models.CharField(max_length=200)
    address= models.CharField(max_length=200)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField(max_length=254, null=True, blank=True)  

def __str__(self):
        return f"{self.first_name} {self.last_name}"
