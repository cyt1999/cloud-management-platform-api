import unittest
from cloud_providers.aliyun import AliyunClient

class TestAliyunClient(unittest.TestCase):

    #执行命令 python manage.py test tests
    def test_get_servers(self):
        # 初始化 AliyunClient
        client = AliyunClient('***', '***', 'cn-hangzhou', 6)

        # 调用 get_servers 方法并打印返回值
        result = client.get_servers()
        print(result)

    def test_get_domains(self):
        # 初始化 AliyunClient
        client = AliyunClient('***', '***', 'cn-hangzhou', 6)

        # 调用 get_domains 方法并打印返回值
        result = client.get_domains()
        print(result)

if __name__ == '__main__':
    unittest.main() 