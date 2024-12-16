import logging
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger
from django_apscheduler.jobstores import DjangoJobStore, register_events, register_job
from CloudServerApp.management.commands.sync_cloud_data import Command as SyncCloudDataCommand
from NotificationApp.tasks import check_expiring_resources
from django.conf import settings

# 配置日志
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def start():
    scheduler = BackgroundScheduler(timezone=settings.SCHEDULER_TIMEZONE)
    scheduler.add_jobstore(DjangoJobStore(), "default")

    # 每天凌晨2点执行同步任务
    @register_job(scheduler, CronTrigger(hour="2", minute="0", second="0"), id="sync_cloud_data", replace_existing=True)
    def sync_cloud_data():
        logger.info("开始执行数据同步任务...")
        try:
            command = SyncCloudDataCommand()
            command.handle()
            logger.info("数据同步任务执行完成")
        except Exception as e:
            logger.error(f"数据同步任务执行失败: {str(e)}")

    # 每天早上9点检查过期资源并发送通知
    @register_job(scheduler, CronTrigger(hour="9", minute="0", second="0"), id="check_expiring_resources", replace_existing=True)
    def check_resources():
        logger.info("开始检查资源到期情况...")
        try:
            check_expiring_resources()
            logger.info("资源到期检查完成")
        except Exception as e:
            logger.error(f"资源到期检查失败: {str(e)}")

    register_events(scheduler)
    scheduler.start()
    logger.info("调度器已启动...") 