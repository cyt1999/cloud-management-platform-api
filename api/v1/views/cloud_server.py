from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from apps.cloud_server.models import CloudServer
from apps.cloud_server.serializers import CloudServerSerializer

class CloudServerViewSet(viewsets.ModelViewSet):
    queryset = CloudServer.objects.all()
    serializer_class = CloudServerSerializer

    @action(detail=False)
    def expiring_soon(self, request):
        # 实现获取即将到期服务器的逻辑
        pass 