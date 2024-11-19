from django.apps import AppConfig

class CloudmanagementplatformapiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'CloudManagementPlatformApi'

    def ready(self):
        # 确保调度器在应用程序准备好时启动
        from . import scheduler
        scheduler.start() 