from django.apps import AppConfig

class SchedulerConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.scheduler'
    verbose_name = '调度器' 