import os
from alibabacloud_tea_openapi.models import Config
from alibabacloud_ecs20140526.client import Client as Ecs20140526Client
from alibabacloud_tea_util import models as util_models
from alibabacloud_ecs20140526 import models as ecs_20140526_models
from Tea.exceptions import UnretryableException, TeaException
from CloudServerApp.models import CloudServer
from CustomerApp.models import Customer
import json

class AliyunClient:
    def __init__(self, access_key_id, access_key_secret, region, customer_id):
        self.access_key_id = access_key_id
        self.access_key_secret = access_key_secret
        self.region = region
        self.customer_id = customer_id
        self.client = self.create_client()

    def create_client(self) -> Ecs20140526Client:
        """
        使用AK&SK初始化账号Client
        @return: Client
        @throws Exception
        """
        config = Config(
            access_key_id=self.access_key_id,
            access_key_secret=self.access_key_secret,
            endpoint=f'ecs.{self.region}.aliyuncs.com'
        )
        return Ecs20140526Client(config)

    def get_servers(self):
        '''
        获取阿里云服务器信息并存入数据库
        '''
        describe_instances_request = ecs_20140526_models.DescribeInstancesRequest(
            region_id=self.region
        )
        runtime = util_models.RuntimeOptions()
        try:
            response = self.client.describe_instances_with_options(describe_instances_request, runtime)
            #json返回值转字典
            instances = response.body.instances.instance
            customer = Customer.objects.get(id=self.customer_id)
            #遍历实例
            for instance in instances:
                # 更新或创建云服务器信息
                CloudServer.objects.update_or_create(
                    instance_id=instance.instance_id,
                    defaults={
                        'status': instance.status,
                        'public_ip_address': instance.public_ip_address.ip_address[0],
                        'private_ip_address': instance.network_interfaces.network_interface[0].primary_ip_address,
                        'cpu': instance.cpu,
                        'memory': instance.memory / 1024,  # 内存单位是MB
                        'instance_charge_type': instance.instance_charge_type, # PrePaid：包年包月。PostPaid：按量付费。
                        'creation_time': instance.creation_time,
                        'expired_time': instance.expired_time,
                        'customer': customer
                    }
                )
            return "Success"
        except (UnretryableException, TeaException, Exception) as e:
            return f"Error fetching instances: {e}"

    def get_domains(self):
        '''
        获取阿里云域名信息
        '''
        return [
            {
                'domain_name': 'example.com',
                'domain_status': 'active',
                'real_name_auth_status': 'verified',
                'registration_date': '2023-01-01',
                'expiration_date': '2024-01-01'
            },
            # 更多域名信息
        ] 