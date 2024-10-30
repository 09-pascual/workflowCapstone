from django.db import models
from .group import Group
from .user import User

class GroupWorker(models.Model):
    group_id = models.ForeignKey(
        Group,
        on_delete=models.CASCADE,
        related_name='group_workers',
        null=True
    )
    worker_id = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='group_assignments',
        default=1
    )

    class Meta:
        db_table = 'workflowapi_groupworker'
        unique_together = ['group_id', 'worker_id']  # Make sure this matches your field names

    def __str__(self):
        return f"{self.worker_id.user_name} - {self.group_id.name}"