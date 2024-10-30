from rest_framework import serializers
from rest_framework import viewsets
from workflowapi.models import ProjectWorker
from .user import UserSerializer

class ProjectWorkerSerializer(serializers.HyperlinkedModelSerializer):
    worker = UserSerializer(source='worker_id', read_only=True)
    
    class Meta:
        model = ProjectWorker
        fields = ('id', 'url', 'project_id', 'worker_id', 'worker')

class ProjectWorkerViewSet(viewsets.ModelViewSet):
    queryset = ProjectWorker.objects.all()
    serializer_class = ProjectWorkerSerializer