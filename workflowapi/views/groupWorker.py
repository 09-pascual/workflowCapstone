from rest_framework import serializers
from rest_framework import viewsets
from workflowapi.models import GroupWorker


class GroupWorkerSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = GroupWorker
        fields = ('id', 'url', 'group', 'worker')
        
class GroupWorkerViewSet(viewsets.ModelViewSet):
    
    queryset = GroupWorker.objects.all()
    serializer_class = GroupWorkerSerializer