from rest_framework import serializers
from rest_framework import viewsets
from workflowapi.models import Worker

class WorkerSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = Worker
        fields = ('id', 'url', 'user', 'availability')
        

class WorkerViewSet(viewsets.ModelViewSet):
    
    queryset = Worker.objects.all()
    serializer_class = WorkerSerializer