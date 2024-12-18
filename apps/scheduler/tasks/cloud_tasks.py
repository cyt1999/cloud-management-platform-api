from django.core.management.base import BaseCommand
from apps.customer.models import Customer
from apps.cloud_server.models import CloudServer
from common.utils.cloud_providers.aliyun import AliyunClient
from common.utils.cloud_providers.volcengine import VolcengineClient
import logging

logger = logging.getLogger(__name__)

def sync_cloud_servers():
    """同步云服务器数据"""
    logger.info("开始同步云服务器数据...")
    customers = Customer.objects.all()
    
    for customer in customers:
        try:
            if customer.cloud_platform_type == 'aliyun':
                client = AliyunClient(customer.access_key_id, customer.access_key_secret, customer.regions, customer.id)
            elif customer.cloud_platform_type == 'volcengine':
                client = VolcengineClient(customer.access_key_id, customer.access_key_secret, customer.regions, customer.id)
            else:
                logger.warning(f"Unsupported platform: {customer.cloud_platform_type}")
                continue

            servers = client.get_servers()
            # for server in servers:
            #     CloudServer.objects.update_or_create(
            #         instance_id=server['instance_id'],
            #         defaults={
            #             'instance_name': server['instance_name'],
            #             'status': server['status'],
            #             'specification': server['specification'],
            #             'ip_address': server['ip_address'],
            #             'customer': customer
            #         }
            #     )
            logger.info(f"Successfully synced servers for customer: {customer.name}")
        except Exception as e:
            logger.error(f"Failed to sync servers for customer {customer.name}: {str(e)}") 