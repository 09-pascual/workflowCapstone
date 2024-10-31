# views/group.py
from rest_framework import serializers
from rest_framework import viewsets
from workflowapi.models import Group
from .user import UserSerializer 

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    workers = UserSerializer(many=True, read_only=False)
    
    class Meta:
        model = Group
        fields = ('id', 'url', 'name', 'description', 'workers')
        
class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer