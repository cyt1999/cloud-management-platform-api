from django.utils import timezone
from datetime import timedelta
from apps.cloud_server.models import CloudServer
from apps.domain.models import Domain
from .services import NotificationService

def check_expiring_resources():
    """检查即将到期的资源并发送通知"""
    notification_service = NotificationService()
    days_threshold = 7
    current_time = timezone.now()
    threshold_date = current_time + timedelta(days=days_threshold)
    
    # 检查即将到期的服务器
    expiring_servers = CloudServer.objects.filter(
        expired_time__lte=threshold_date
    ).exclude(expired_time__isnull=True)
    
    # 检查即将到期的域名
    expiring_domains = Domain.objects.filter(
        expiration_date__lte=threshold_date
    ).exclude(expiration_date__isnull=True)
    
    if expiring_servers or expiring_domains:
        content = "以下资源即将到期：\n\n"
        
        if expiring_servers:
            content += "服务器：\n"
            for server in expiring_servers:
                days_left = (server.expired_time - current_time).days
                content += f"- {server.instance_id}: 还有{days_left}天到期\n"
        
        if expiring_domains:
            content += "\n域名：\n"
            for domain in expiring_domains:
                days_left = (domain.expiration_date - current_time).days
                content += f"- {domain.domain_name}: 还有{days_left}天到期\n"
        
        notification_service.send_notification(
            title="资源到期提醒",
            content=content,
            receivers=["admin@example.com"]
        ) 