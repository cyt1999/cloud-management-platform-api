from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from apps.customer.models import Customer
from apps.cloud_server.models import CloudServer
from apps.domain.models import Domain

class APIEndpointsTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        # 创建测试数据
        self.customer = Customer.objects.create(
            name="Test Customer",
            cloud_platform_type="aliyun",
            account="test_account",
            access_key_id="test_key",
            access_key_secret="test_secret",
            regions=["cn-hangzhou"]
        )

    def test_customer_endpoints(self):
        # 测试获取客户列表
        response = self.client.get(reverse('customer-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # 测试创建客户
        data = {
            "name": "New Customer",
            "cloud_platform_type": "aliyun",
            "account": "new_account",
            "access_key_id": "new_key",
            "access_key_secret": "new_secret",
            "regions": ["cn-beijing"]
        }
        response = self.client.post(reverse('customer-list'), data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_cloud_server_endpoints(self):
        # 测试获取服务器列表
        response = self.client.get(reverse('cloudserver-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # 测试获取即将到期的服务器
        response = self.client.get(reverse('cloudserver-expiring-soon'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_domain_endpoints(self):
        # 测试获取域名列表
        response = self.client.get(reverse('domain-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # 测试获取即将到期的域名
        response = self.client.get(reverse('domain-expiring-soon'))
        self.assertEqual(response.status_code, status.HTTP_200_OK) 