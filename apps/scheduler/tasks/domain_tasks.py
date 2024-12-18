from apps.customer.models import Customer
from apps.domain.models import Domain
from common.utils.cloud_providers.aliyun import AliyunClient
from common.utils.cloud_providers.volcengine import VolcengineClient
import logging

logger = logging.getLogger(__name__)

def sync_domains():
    """同步域名数据"""
    logger.info("开始同步域名数据...")
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

            domains = client.get_domains()
            # for domain in domains:
            #     Domain.objects.update_or_create(
            #         domain_name=domain['domain_name'],
            #         defaults={
            #             'domain_status': domain['domain_status'],
            #             'real_name_auth_status': domain['real_name_auth_status'],
            #             'registration_date': domain['registration_date'],
            #             'expiration_date': domain['expiration_date'],
            #             'customer': customer
            #         }
            #     )
            logger.info(f"Successfully synced domains for customer: {customer.name}")
        except Exception as e:
            logger.error(f"Failed to sync domains for customer {customer.name}: {str(e)}") 