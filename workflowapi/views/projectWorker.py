from rest_framework import serializers
from rest_framework import viewsets
from workflowapi.models import ProjectWorker

class ProjectWorkerSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = ProjectWorker
        fields = ('id', 'url', 'project', 'worker')
        
        
class ProjectWorkerViewSet(viewsets.ModelViewSet):
    
    queryset = ProjectWorker.objects.all()
    serializer_class = ProjectWorkerSerializer