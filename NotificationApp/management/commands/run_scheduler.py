from django.core.management.base import BaseCommand
from CloudManagementPlatformApi.scheduler import start
import time

class Command(BaseCommand):
    help = '启动调度器'

    def handle(self, *args, **options):
        self.stdout.write('Starting scheduler...')
        try:
            start()
            # 保持进程运行
            while True:
                time.sleep(60)
        except (KeyboardInterrupt, SystemExit):
            self.stdout.write('Stopping scheduler...') 