from django.test import TestCase
from common.utils.cloud_providers.aliyun import AliyunClient
from common.utils.cloud_providers.volcengine import VolcengineClient

class TestAliyunClient(TestCase):
    def setUp(self):
        self.client = AliyunClient('test_key', 'test_secret', 'cn-hangzhou', 1)

    def test_get_servers(self):
        result = self.client.get_servers()
        self.assertIsInstance(result, list)

    def test_get_domains(self):
        result = self.client.get_domains()
        self.assertIsInstance(result, list)

class TestVolcengineClient(TestCase):
    def setUp(self):
        self.client = VolcengineClient('test_key', 'test_secret', 'cn-north-1', 1)

    def test_get_servers(self):
        result = self.client.get_servers()
        self.assertIsInstance(result, list)

    def test_get_domains(self):
        result = self.client.get_domains()
        self.assertIsInstance(result, list) 