from django.db import models
from .group import Group
from .user import User

class GroupWorker(models.Model):
    group = models.ForeignKey(
        Group, 
        on_delete=models.CASCADE,
        related_name='group_workers'
    )
    worker = models.ForeignKey(
        User, 
        on_delete=models.CASCADE,
        related_name='group_assignments',
        default=1  
    )

    class Meta:
        db_table = 'workflowapi_groupworker'
        unique_together = ['group', 'worker']

    def __str__(self):
        return f"{self.worker.user_name} - {self.group.name}"