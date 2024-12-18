import os
from alibabacloud_tea_openapi.models import Config
from alibabacloud_ecs20140526.client import Client as Ecs20140526Client
from alibabacloud_domain20180129.client import Client as Domain20180129Client
from alibabacloud_tea_util import models as util_models
from alibabacloud_ecs20140526 import models as ecs_20140526_models
from alibabacloud_domain20180129 import models as domain_20180129_models
from Tea.exceptions import UnretryableException, TeaException
from apps.cloud_server.models import CloudServer
from apps.customer.models import Customer
from apps.domain.models import Domain
from zoneinfo import ZoneInfo
from datetime import datetime
import logging

logger = logging.getLogger(__name__)

class AliyunClient:
    def __init__(self, access_key_id, access_key_secret, regions, customer_id):
        self.access_key_id = access_key_id
        self.access_key_secret = access_key_secret
        self.regions = regions
        self.customer_id = customer_id
        self.ecs_clients = {region: self.create_ecs_client(region) for region in regions}  # 为每个地域创建客户端
        self.domain_client = self.create_domain_client()

    def create_ecs_client(self, region) -> Ecs20140526Client:
        """
        使用AK&SK初始化ECS账号Client
        @param region: 地域ID
        @return: Client
        @throws Exception
        """
        config = Config(
            access_key_id=self.access_key_id,
            access_key_secret=self.access_key_secret,
            endpoint=f'ecs.{region}.aliyuncs.com'
        )
        return Ecs20140526Client(config)

    def create_domain_client(self) -> Domain20180129Client:
        """
        使用AK&SK初始化域名账号Client
        @return: Client
        @throws Exception
        """
        config = Config(
            access_key_id=self.access_key_id,
            access_key_secret=self.access_key_secret,
            endpoint='domain.aliyuncs.com'
        )
        return Domain20180129Client(config)

    def get_servers(self):
        '''
        获取所有地域的阿里云服务器信息并存入数据库
        '''
        all_instances = []
        for region in self.regions:
            describe_instances_request = ecs_20140526_models.DescribeInstancesRequest(
                region_id=region
            )
            runtime = util_models.RuntimeOptions()
            try:
                response = self.ecs_clients[region].describe_instances_with_options(describe_instances_request, runtime)
                instances = response.body.instances.instance
                customer = Customer.objects.get(id=self.customer_id)
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
                all_instances.extend(instances)
            except (UnretryableException, TeaException, Exception) as e:
                print(f"Error fetching instances in {region}: {e}")
        return "Success"

    def get_domains(self):
        '''
        获取阿里云域名信息并存入数据库
        '''
        # 获取20个域名足够了，正常来说都不会超过这个数量
        query_domain_list_request = domain_20180129_models.QueryDomainListRequest(
            page_num=1,
            page_size=20
        )
        runtime = util_models.RuntimeOptions()
        try:
            response = self.domain_client.query_domain_list_with_options(query_domain_list_request, runtime)
            domains = response.body.data.domain  # 获取域名信息
            customer = Customer.objects.get(id=self.customer_id) # 获取客户信息
            for domain in domains:
                # 先将字符串转换为 datetime 对象
                registration_date = datetime.strptime(domain.registration_date, '%Y-%m-%d %H:%M:%S')
                expiration_date = datetime.strptime(domain.expiration_date, '%Y-%m-%d %H:%M:%S')
                
                # 然后添加时区信息
                registration_date = registration_date.replace(tzinfo=ZoneInfo('Asia/Shanghai'))
                expiration_date = expiration_date.replace(tzinfo=ZoneInfo('Asia/Shanghai'))
                # 更新或创建域名信息
                Domain.objects.update_or_create(
                    domain_name=domain.domain_name,
                    defaults={
                        # 域名状态 1：急需续费。2：急需赎回。3：正常。
                        'domain_status': domain.domain_status,
                        # 域名持有人
                        'ccompany': domain.ccompany, 
                        # 注册时间  # 处理日期时间并添加时区信息
                        'registration_date':  registration_date,
                        # 到期时间  # 处理日期时间并添加时区信息
                        'expiration_date': expiration_date,
                        # 到期时间差
                        'expiration_curr_date_diff': domain.expiration_curr_date_diff,
                        # 关联的客户
                        'customer': customer    
                    }
                )
            print("domains:", domains)
            return "Success"
        except (UnretryableException, TeaException, Exception) as e:
            return f"Error fetching domains: {e}" 