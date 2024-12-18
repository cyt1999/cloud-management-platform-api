from django.core.management.base import BaseCommand
from apps.scheduler.scheduler import start
import time
import logging

logger = logging.getLogger(__name__)

class Command(BaseCommand):
    help = '启动系统调度器'

    def handle(self, *args, **options):
        self.stdout.write('Starting system scheduler...')
        logger.info('Starting system scheduler...')
        try:
            start()
            while True:
                time.sleep(60)
        except (KeyboardInterrupt, SystemExit):
            self.stdout.write('Stopping system scheduler...')
            logger.info('Stopping system scheduler...') 