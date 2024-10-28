from rest_framework import serializers
from rest_framework import viewsets
from workflowapi.models import Invoice

class InvoiceSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = Invoice
        fields = ('id', 'url', 'project', 'amount', 'amount', 'status', 'issue_date', 'due_date')
        

class InvoiceViewSet(viewsets.ModelViewSet):
    
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer