from django.test import TestCase
from apps.scheduler.scheduler import start, shutdown
from apps.scheduler.tasks.cloud_tasks import sync_cloud_servers
from apps.scheduler.tasks.domain_tasks import sync_domains
from unittest.mock import patch
from apps.customer.models import Customer
from apps.cloud_server.models import CloudServer
from apps.domain.models import Domain

class TestScheduler(TestCase):
    def setUp(self):
        # 移除调度器的启动，避免数据库锁定
        pass

    def tearDown(self):
        # 确保调度器被正确关闭
        shutdown()

    @patch('apps.scheduler.tasks.cloud_tasks.sync_cloud_servers')
    def test_sync_cloud_servers_job(self, mock_sync):
        """测试云服务器同步任务"""
        sync_cloud_servers()
        mock_sync.assert_called_once()

    @patch('apps.scheduler.tasks.domain_tasks.sync_domains')
    def test_sync_domains_job(self, mock_sync):
        """测试域名同步任务"""
        sync_domains()
        mock_sync.assert_called_once()

    @patch('apps.scheduler.tasks.cloud_tasks.sync_cloud_servers')
    def test_sync_cloud_servers_with_exception(self, mock_sync):
        """测试云服务器同步任务出现异常的情况"""
        mock_sync.side_effect = Exception("同步失败")
        with self.assertRaises(Exception):
            sync_cloud_servers()
        mock_sync.assert_called_once()

    @patch('apps.scheduler.tasks.domain_tasks.sync_domains')
    def test_sync_domains_with_exception(self, mock_sync):
        """测试域名同步任务出现异常的情况"""
        mock_sync.side_effect = Exception("同步失败")
        with self.assertRaises(Exception):
            sync_domains()
        mock_sync.assert_called_once()

    @patch('apps.scheduler.tasks.cloud_tasks.sync_cloud_servers')
    def test_sync_cloud_servers_no_resources(self, mock_sync):
        """测试云服务器同步任务没有可同步资源的情况"""
        Customer.objects.create(
            name="Test Customer",
            cloud_platform_type="aliyun",
            access_key_id="test_key",
            access_key_secret="test_secret",
            regions=["cn-hangzhou"]
        )
        mock_sync.return_value = []  # 模拟没有资源
        sync_cloud_servers()
        mock_sync.assert_called_once()

    @patch('apps.scheduler.tasks.domain_tasks.sync_domains')
    def test_sync_domains_no_resources(self, mock_sync):
        """测试域名同步任务没有可同步资源的情况"""
        Customer.objects.create(
            name="Test Customer",
            cloud_platform_type="aliyun",
            access_key_id="test_key",
            access_key_secret="test_secret",
            regions=["cn-hangzhou"]
        )
        mock_sync.return_value = []  # 模拟没有资源
        sync_domains()
        mock_sync.assert_called_once()