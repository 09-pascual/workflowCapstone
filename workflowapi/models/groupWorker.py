from django.db import models
from .group import Group
from .worker import Worker

class GroupWorker(models.Model):
    
    group_id = models.ForeignKey(
        Group,
        on_delete=models.CASCADE,
        related_name='group_workers'
    )
    worker_id = models.ForeignKey(
        Worker,
        on_delete=models.CASCADE,
        related_name='worker_groups',
        
    )

    class Meta:
        unique_together = ['group_id', 'worker_id']

    def __str__(self):
        return f"{self.worker_id.user.user_name} - {self.group_id.name}"