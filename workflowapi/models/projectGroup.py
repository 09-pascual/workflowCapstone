from django.db import models
from .project import Project
from .group import Group

class ProjectGroup(models.Model):
    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        related_name='project_groups'
    )
    group = models.ForeignKey(
        Group,
        on_delete=models.CASCADE,
        related_name='assigned_group_projects'
    )

    class Meta:
        unique_together = ['project', 'group']