from .base import *

DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1', 'localhost']

# 开发环境特定配置 

# 开发环境特定的日志配置
LOGGING['loggers']['django']['level'] = 'DEBUG'
LOGGING['loggers']['apps']['level'] = 'DEBUG'

# 开发环境下的邮件配置
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'