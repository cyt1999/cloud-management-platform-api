from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from django.utils import timezone
from datetime import timedelta
from .models import CloudServer, MonitoringData
from .serializers import CloudServerSerializer, MonitoringDataSerializer

class CloudServerViewSet(viewsets.ModelViewSet):
    queryset = CloudServer.objects.all()
    serializer_class = CloudServerSerializer

    @action(detail=False, methods=['get'])
    def expiring_soon(self, request):
        """获取即将到期的服务器列表"""
        days_threshold = int(request.query_params.get('days', 7))
        current_time = timezone.now()
        threshold_date = current_time + timedelta(days=days_threshold)
        
        expiring_servers = CloudServer.objects.filter(
            expired_time__lte=threshold_date
        ).exclude(expired_time__isnull=True)
        
        serializer = self.get_serializer(expiring_servers, many=True)
        return Response({
            'days_threshold': days_threshold,
            'count': expiring_servers.count(),
            'servers': serializer.data
        })

class MonitoringDataViewSet(viewsets.ModelViewSet):
    queryset = MonitoringData.objects.all()
    serializer_class = MonitoringDataSerializer 