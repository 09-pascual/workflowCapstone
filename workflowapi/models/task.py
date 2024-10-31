from django.db import models
from .project import Project
from .worker import Worker


class Task(models.Model):
    
    TASK_STATUS = [
        ('Pending', 'Pending'),
        ('InProgress', 'InProgress'),
        ('Completed', 'Completed')
    ]
    
    project_id = models.ForeignKey(Project, on_delete=models.CASCADE)
    worker_id = models.ForeignKey(Worker, on_delete=models.CASCADE)
    description = models.TextField()
    status= models.CharField(max_length=15, choices=TASK_STATUS)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    
    
    