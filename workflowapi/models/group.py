from django.db import models
from .user import User  

class Group(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    workers = models.ManyToManyField(
        User,
        related_name='workflow_groups',
        through='GroupWorker'

    )

    def __str__(self):
        return self.name