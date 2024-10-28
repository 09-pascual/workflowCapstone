from rest_framework import serializers
from rest_framework import viewsets
from workflowapi.models import ProjectGroup


class ProjectGroupSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = ProjectGroup
        fields = ('id', 'url', 'project', 'group')
        

class ProjectGroupViewSet(viewsets.ModelViewSet):
    
    queryset = ProjectGroup.objects.all()
    serializer_class = ProjectGroupSerializer