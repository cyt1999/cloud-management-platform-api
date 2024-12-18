from rest_framework import viewsets
from .models import Customer
from .serializers import CustomerCreateSerializer, CustomerRetrieveSerializer

class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()

    def get_serializer_class(self):
        if self.request.method in ['POST', 'PUT']:
            return CustomerCreateSerializer
        return CustomerRetrieveSerializer 