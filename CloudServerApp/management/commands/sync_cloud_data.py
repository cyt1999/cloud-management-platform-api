from django.core.management.base import BaseCommand
from CustomerApp.models import Customer
from CloudServerApp.models import CloudServer
from DomainApp.models import Domain

from cloud_providers.aliyun import AliyunClient
from cloud_providers.volcengine import VolcengineClient

class Command(BaseCommand):
    help = 'Sync cloud server and domain data from cloud providers'

    def handle(self, *args, **kwargs):
        customers = Customer.objects.all()
        # 遍历所有客户，根据客户类型初始化不同的云平台客户端
        for customer in customers:
            if customer.cloud_platform_type == 'aliyun':
                client = AliyunClient(customer.access_key_id, customer.access_key_secret)
            elif customer.cloud_platform_type == 'volcengine':
                client = VolcengineClient(customer.access_key_id, customer.access_key_secret)
            else:
                self.stdout.write(self.style.WARNING(f"Unsupported platform: {customer.cloud_platform_type}"))
                continue

            # 获取服务器信息并入库
            servers = client.get_servers()
            for server in servers:
                CloudServer.objects.update_or_create(
                    instance_id=server['instance_id'],
                    defaults={
                        'instance_name': server['instance_name'],
                        'status': server['status'],
                        'specification': server['specification'],
                        'ip_address': server['ip_address'],
                        'customer': customer
                    }
                )

            # 获取域名信息并入库
            domains = client.get_domains()
            for domain in domains:
                Domain.objects.update_or_create(
                    domain_name=domain['domain_name'],
                    defaults={
                        'domain_status': domain['domain_status'],
                        'real_name_auth_status': domain['real_name_auth_status'],
                        'registration_date': domain['registration_date'],
                        'expiration_date': domain['expiration_date']
                    }
                )

            self.stdout.write(self.style.SUCCESS(f"Data synced for customer: {customer.name}")) 