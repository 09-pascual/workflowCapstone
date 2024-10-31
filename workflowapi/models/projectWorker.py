from django.db import models
from .worker import Worker
from .project import Project

class ProjectWorker(models.Model):
    project_id = models.ForeignKey(
        Project, 
        on_delete=models.CASCADE,
        related_name='project_workers'
    )
    worker_id = models.ForeignKey(
        Worker, 
        on_delete=models.CASCADE,
        related_name='assigned_projects'
    )

    class Meta:
        unique_together = ['project_id', 'worker_id']

