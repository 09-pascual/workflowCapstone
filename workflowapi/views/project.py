from rest_framework import serializers, viewsets
from workflowapi.models import Project


class ProjectSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Project
        fields = ('id', 'url', 'name', 'description', 'start_date', 'end_date')
        
        
class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer