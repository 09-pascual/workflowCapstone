from django.db import models
from .worker import Worker  

class Group(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    workers = models.ManyToManyField(
        Worker,
        related_name='workflow_groups',
        through='GroupWorker',
        through_fields=('group_id', 'worker_id'),
    )

    def __str__(self):
        return self.name