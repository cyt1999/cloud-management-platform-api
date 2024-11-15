from django.db import models

# 域名模型，存储域名的基本信息
class Domain(models.Model):
    domain_name = models.CharField(max_length=100)  # 域名
    domain_status = models.CharField(max_length=50)  # 域名状态
    real_name_auth_status = models.CharField(max_length=50)  # 实名认证状态
    registration_date = models.DateTimeField()  # 注册时间
    expiration_date = models.DateTimeField()  # 到期时间

    def __str__(self):
        return self.domain_name  # 返回域名作为对象的字符串表示
