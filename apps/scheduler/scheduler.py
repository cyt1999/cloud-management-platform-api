import logging
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger
from django_apscheduler.jobstores import DjangoJobStore, register_events
from django.conf import settings
from .tasks.cloud_tasks import sync_cloud_servers
from .tasks.domain_tasks import sync_domains
from common.utils.notification.tasks import check_expiring_resources

logger = logging.getLogger(__name__)

_scheduler = None

def start():
    """启动调度器"""
    global _scheduler
    if _scheduler is None:
        _scheduler = BackgroundScheduler(timezone=settings.SCHEDULER_TIMEZONE)
        _scheduler.add_jobstore(DjangoJobStore(), "default")

        # 添加定时任务
        _scheduler.add_job(
            sync_cloud_servers,
            CronTrigger(hour="2", minute="0", second="0"),
            id="sync_cloud_servers",
            replace_existing=True
        )

        _scheduler.add_job(
            sync_domains,
            CronTrigger(hour="2", minute="30", second="0"),
            id="sync_domains",
            replace_existing=True
        )

        _scheduler.add_job(
            check_expiring_resources,
            CronTrigger(hour="9", minute="0", second="0"),
            id="check_expiring_resources",
            replace_existing=True
        )
        
        # 添加错误处理
        try:
            register_events(_scheduler)
            _scheduler.start()
            logger.info("调度器已启动...")
        except Exception as e:
            logger.error(f"调度器启动失败: {str(e)}")
            _scheduler = None
            raise
    return _scheduler

def shutdown():
    """关闭调度器"""
    global _scheduler
    if _scheduler and _scheduler.running:
        try:
            _scheduler.shutdown()
            _scheduler = None
            logger.info("调度器已关闭...")
        except Exception as e:
            logger.error(f"调度器关闭失败: {str(e)}") 