from rest_framework import serializers
from rest_framework import viewsets
from workflowapi.models import Task

class TaskSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = Task
        fields = ('id', 'url', 'name', 'description', 'assigned_to', 'status', 'due_date')
        
class TaskViewSet(viewsets.ModelViewSet):
    
    queryset = Task.objects.all()
    serializer_class = TaskSerializer