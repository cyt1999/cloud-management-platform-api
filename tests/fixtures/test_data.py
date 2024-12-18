from apps.customer.models import Customer
from apps.cloud_server.models import CloudServer
from apps.domain.models import Domain
from datetime import datetime, timedelta
from django.utils import timezone

def create_test_data():
    # 创建测试客户
    customer = Customer.objects.create(
        name="Test Customer",
        cloud_platform_type="aliyun",
        account="test_account",
        access_key_id="test_key",
        access_key_secret="test_secret",
        regions=["cn-hangzhou"]
    )

    # 创建测试服务器
    CloudServer.objects.create(
        instance_id="i-test1",
        status="Running",
        public_ip_address="1.2.3.4",
        private_ip_address="10.0.0.1",
        cpu=2,
        memory=4.0,
        instance_charge_type="PostPaid",
        creation_time=timezone.now(),
        expired_time=timezone.now() + timedelta(days=5),
        customer=customer
    )

    # 创建测试域名
    Domain.objects.create(
        domain_name="test.com",
        domain_status="Active",
        ccompany="Test Company",
        registration_date=timezone.now() - timedelta(days=365),
        expiration_date=timezone.now() + timedelta(days=10),
        expiration_curr_date_diff=10,
        customer=customer
    ) 