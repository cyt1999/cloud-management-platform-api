from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from django.utils import timezone
from datetime import timedelta
from .models import Domain
from .serializers import DomainSerializer

class DomainViewSet(viewsets.ModelViewSet):
    queryset = Domain.objects.all()
    serializer_class = DomainSerializer

    @action(detail=False, methods=['get'])
    def expiring_soon(self, request):
        """获取即将到期的域名列表"""
        # 从查询参数获取天数阈值，默认为7天
        days_threshold = int(request.query_params.get('days', 7))
        current_time = timezone.now()
        threshold_date = current_time + timedelta(days=days_threshold)
        
        # 查询即将到期的域名
        expiring_domains = Domain.objects.filter(
            expiration_date__lte=threshold_date
        ).exclude(expiration_date__isnull=True)
        
        # 序列化数据并返回
        serializer = self.get_serializer(expiring_domains, many=True)
        return Response({
            'days_threshold': days_threshold,
            'count': expiring_domains.count(),
            'domains': serializer.data
        })
