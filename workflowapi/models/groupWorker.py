from django.db import models
from .group import Group
from .worker import Worker

class GroupWorker(models.Model):
    
    group_id = models.ForeignKey(Group, on_delete=models.DO_NOTHING)
    worker_id = models.ForeignKey(Worker, on_delete=models.DO_NOTHING)
    