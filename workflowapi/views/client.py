from rest_framework import serializers
from rest_framework import viewsets
from workflowapi.models import Client


class ClientSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = Client
        fields = ('id', 'url', 'first_name', 'last_name',
                  'address', 'phone_number', "email")
        
class ClientViewSet(viewsets.ModelViewSet):
    
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
