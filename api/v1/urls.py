from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views.cloud_server import CloudServerViewSet
from .views.customer import CustomerViewSet
from .views.domain import DomainViewSet

router = DefaultRouter()
router.register(r'cloud-servers', CloudServerViewSet)
router.register(r'customers', CustomerViewSet)
router.register(r'domains', DomainViewSet)

urlpatterns = [
    path('', include(router.urls)),
] 