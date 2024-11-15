from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from CustomerApp.views import CustomerViewSet
from CloudServerApp.views import CloudServerViewSet, MonitoringDataViewSet
from DomainApp.views import DomainViewSet

router = DefaultRouter()
router.register(r'customers', CustomerViewSet)
router.register(r'cloudservers', CloudServerViewSet)
router.register(r'monitoringdata', MonitoringDataViewSet)
router.register(r'domains', DomainViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),  # 使用API路由
]