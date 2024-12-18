import logging
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger
from django_apscheduler.jobstores import DjangoJobStore, register_events
from ...apps.cloud_server.management.commands.sync_cloud_data import Command as SyncCloudDataCommand
from ..notification.tasks import check_expiring_resources
from django.conf import settings

# 配置日志
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def sync_cloud_data():
    logger.info("开始执行数据同步任务...")
    try:
        command = SyncCloudDataCommand()
        command.handle()
        logger.info("数据同步任务执行完成")
    except Exception as e:
        logger.error(f"数据同步任务执行失败: {str(e)}")

def check_resources():
    logger.info("开始检查资源到期情况...")
    try:
        check_expiring_resources()
        logger.info("资源到期检查完成")
    except Exception as e:
        logger.error(f"资源到期检查失败: {str(e)}")

_scheduler = None

def start():
    global _scheduler
    if _scheduler is None:
        _scheduler = BackgroundScheduler(timezone=settings.SCHEDULER_TIMEZONE)
        _scheduler.add_jobstore(DjangoJobStore(), "default")

        # 每天凌晨2点执行同步任务
        _scheduler.add_job(sync_cloud_data, CronTrigger(hour="2", minute="0", second="0"), 
                         id="sync_cloud_data", replace_existing=True)

        # 每天早上9点检查过期资源并发送通知
        _scheduler.add_job(check_resources, CronTrigger(hour="9", minute="0", second="0"), 
                         id="check_expiring_resources", replace_existing=True)

        register_events(_scheduler)
        _scheduler.start()
        logger.info("调度器已启动...")
    return _scheduler

def shutdown():
    global _scheduler
    if _scheduler:
        _scheduler.shutdown()
        _scheduler = None
        logger.info("调度器已关闭...")