from django.db import models
from .project import Project
from .worker import Worker

class ProjectWorker(models.Model):
    project_id = models.ForeignKey(Project, on_delete=models.DO_NOTHING)
    worker_id = models.ForeignKey(Worker, on_delete=models.DO_NOTHING)