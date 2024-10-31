from rest_framework import serializers
from rest_framework import viewsets
from workflowapi.models import Project
from .group import GroupSerializer  
from .client import ClientSerializer 

class ProjectSerializer(serializers.HyperlinkedModelSerializer):
    clientId = ClientSerializer(read_only=False)
    assigned_group = GroupSerializer(read_only=False)  
    
    class Meta:
        model = Project
        fields = ('id', 'url', 'clientId', 'assigned_group', 'project_name', 
                 'status', 'start_date', 'end_date', 'expected_duration')
        depth = 1

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer