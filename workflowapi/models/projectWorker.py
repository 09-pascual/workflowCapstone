from django.db import models
from .user import User
from .project import Project

class ProjectWorker(models.Model):
    project_id = models.ForeignKey(
        Project, 
        on_delete=models.CASCADE,
        related_name='project_workers'
    )
    worker_id = models.ForeignKey(
        User, 
        on_delete=models.CASCADE,
        related_name='project_assignments'
    )

    class Meta:
        unique_together = ['project_id', 'worker_id']

    def __str__(self):
        return f"{self.worker_id.user_name} - {self.project_id.project_name}"