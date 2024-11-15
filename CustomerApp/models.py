from django.db import models

# 客户模型，存储客户的基本信息
class Customer(models.Model):
    name = models.CharField(max_length=100)  # 客户名称
    cloud_platform_type = models.CharField(max_length=100)  # 云平台类型
    account = models.CharField(max_length=100)  # 账号
    password = models.CharField(max_length=100)  # 密码
    key = models.CharField(max_length=100)  # 密钥

    def __str__(self):
        return self.name  # 返回客户名称作为对象的字符串表示 