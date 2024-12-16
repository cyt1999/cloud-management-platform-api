from django.apps import AppConfig

class CloudmanagementplatformapiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'CloudManagementPlatformApi'

    def ready(self):
        # 移除自动启动调度器的代码,确保在数据库迁移完成后再启动调度器
        pass 