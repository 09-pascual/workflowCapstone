from django.db import models
from .project import Project

class Invoice(models.Model):
    
    STATUS_CHOICES= [
        ('Paid', 'Paid'),
        ('Pending', 'Pending'),
        ('Overdue', 'Overdue')
    ]
    
    project_id = models.ForeignKey(Project, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)
    issue_date = models.DateTimeField()
    due_date = models.DateTimeField()
    

