from rest_framework import serializers
from rest_framework import viewsets
from workflowapi.models import Task

class TaskSerializer(serializers.HyperlinkedModelSerializer):
    project_name = serializers.CharField(source='project_id.project_name', read_only=True)
    worker_name = serializers.CharField(source='worker_id.user.user_name', read_only=True)
   
    class Meta:
        model = Task
        fields = ('id', 'url', 'project_id', 'worker_id',  
                  'description', 'status', 'start_date', 'end_date', 'project_name', 'worker_name')
        
class TaskViewSet(viewsets.ModelViewSet):
    
    queryset = Task.objects.all()
    serializer_class = TaskSerializer