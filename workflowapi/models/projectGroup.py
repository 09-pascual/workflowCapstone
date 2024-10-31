from django.db import models
from .project import Project
from .group import Group

class ProjectGroup(models.Model):
    
    project_id = models.ForeignKey(Project, on_delete=models.CASCADE)
    group_id = models.ForeignKey(Group, on_delete=models.CASCADE)
    
    