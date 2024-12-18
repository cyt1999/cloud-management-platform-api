from django.core.management.base import BaseCommand
from apps.scheduler.tasks.cloud_tasks import sync_cloud_servers
from apps.scheduler.tasks.domain_tasks import sync_domains
from common.utils.notification.tasks import check_expiring_resources
import logging

logger = logging.getLogger(__name__)

class Command(BaseCommand):
    help = '测试调度任务'

    def handle(self, *args, **options):
        try:
            self.stdout.write('Testing sync_cloud_servers...')
            sync_cloud_servers()
            
            self.stdout.write('Testing sync_domains...')
            sync_domains()
            
            self.stdout.write('Testing check_expiring_resources...')
            check_expiring_resources()
            
            self.stdout.write(self.style.SUCCESS('All tasks completed successfully'))
            
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error: {str(e)}'))
            logger.error(f'Task execution failed: {str(e)}')