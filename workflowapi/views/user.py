from rest_framework import serializers
from rest_framework import viewsets
from workflowapi.models import User

class UserSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = User
        fields = ('id', 'url', 'user_name', 'first_name', 'last_name',
                  'birthdate', 'phone_number', 'role' )
        
class UserViewSet(viewsets.ModelViewSet):
    
    queryset = User.objects.all()
    serializer_class = UserSerializer