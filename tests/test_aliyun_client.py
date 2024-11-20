import unittest
from cloud_providers.aliyun import AliyunClient

class TestAliyunClient(unittest.TestCase):

    #执行命令 python manage.py test tests
    def test_get_servers(self):
        # 初始化 AliyunClient
        client = AliyunClient('***', '***', '***', 0)

        # 调用 get_servers 方法并打印返回值
        result = client.get_servers()
        print(result)

if __name__ == '__main__':
    unittest.main() 