from rest_framework import serializers
from rest_framework import viewsets
from workflowapi.models import User

class UserSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = User
        fields = ('id', 'url', 'username', 'email', 'first_name', 'last_name')
        
class UserViewSet(viewsets.ModelViewSet):
    
    queryset = User.objects.all()
    serializer = User.objects.all()