from rest_framework import serializers
from rest_framework import viewsets
from workflowapi.models import ProjectWorker
from .user import UserSerializer
from .project import ProjectSerializer  # Import ProjectSerializer

class ProjectWorkerSerializer(serializers.HyperlinkedModelSerializer):
    worker_details = UserSerializer(source='worker_id', read_only=True)
    project_details = ProjectSerializer(source='project_id', read_only=True)
    
    class Meta:
        model = ProjectWorker
        fields = ('id', 'url', 'project_id', 'worker_id', 
                 'worker_details', 'project_details')

class ProjectWorkerViewSet(viewsets.ModelViewSet):
    queryset = ProjectWorker.objects.all()
    serializer_class = ProjectWorkerSerializer