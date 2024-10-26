from rest_framework import serializers
from rest_framework import viewsets
from workflowapi.models import Group

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = Group
        fields = ('id', 'url', 'name', 'description')
        

class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer