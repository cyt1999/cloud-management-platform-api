"""
URL configuration for CloudManagementPlatformApi project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from CustomerApp.views import CustomerViewSet
from CloudServerApp.views import CloudServerViewSet, MonitoringDataViewSet
from DomainApp.views import DomainViewSet
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

router = DefaultRouter()
router.register(r'customers', CustomerViewSet)
router.register(r'cloudservers', CloudServerViewSet)
router.register(r'monitoringdata', MonitoringDataViewSet)
router.register(r'domains', DomainViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),  # 使用API路由
    path('api/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'), # 登陆接口
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # 刷新令牌
]
