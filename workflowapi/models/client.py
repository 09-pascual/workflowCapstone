from django.db import models


class Client(models.Model):
    first_name= models.CharField(max_length=200)
    last_name= models.CharField(max_length=200)
    address= models.CharField(max_length=200)
    phone_number = models.CharField(max_length=15)
