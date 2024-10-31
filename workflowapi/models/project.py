from django.db import models
from .client import Client
from .group import Group
from .worker import Worker

class Project(models.Model):
    STATUS_CHOICES = [
        ('Open', 'Open'),
        ('Closed', 'Closed'),
        ('Upcoming', 'Upcoming'),
    ]
    
    clientId = models.ForeignKey(Client, on_delete=models.CASCADE)
    assigned_group = models.ForeignKey(
        Group,
        on_delete=models.CASCADE,
        null=True,
        related_name='assigned_projects'
    )
    project_name = models.CharField(max_length=200)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    expected_duration = models.IntegerField()
    workers = models.ManyToManyField(
        Worker,
        through='ProjectWorker',
        through_fields=('project_id', 'worker_id'),
        related_name='worker_projects'
    )
    groups = models.ManyToManyField(
        Group,
        through='ProjectGroup',
        related_name='group_projects'
    )

    def __str__(self):
        return self.project_name