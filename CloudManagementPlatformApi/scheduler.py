from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger
from django_apscheduler.jobstores import DjangoJobStore, register_events, register_job
from CloudServerApp.management.commands.sync_cloud_data import Command as SyncCloudDataCommand

def start():
    scheduler = BackgroundScheduler()
    scheduler.add_jobstore(DjangoJobStore(), "default")

    # 每天凌晨2点执行同步任务
    @register_job(scheduler, CronTrigger(hour="2", minute="0", second="0"), id="sync_cloud_data", replace_existing=True)
    def sync_cloud_data():
        command = SyncCloudDataCommand()
        command.handle()

    register_events(scheduler)
    scheduler.start()
    print("Scheduler started...") 