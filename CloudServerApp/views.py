from rest_framework import viewsets
from .models import CloudServer, MonitoringData
from .serializers import CloudServerSerializer, MonitoringDataSerializer

class CloudServerViewSet(viewsets.ModelViewSet):
    queryset = CloudServer.objects.all()
    serializer_class = CloudServerSerializer

class MonitoringDataViewSet(viewsets.ModelViewSet):
    queryset = MonitoringData.objects.all()
    serializer_class = MonitoringDataSerializer
