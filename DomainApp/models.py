from django.db import models
from CustomerApp.models import Customer

# 域名模型，存储域名的基本信息
class Domain(models.Model):
    domain_name = models.CharField(max_length=100)  # 域名
    domain_status = models.CharField(max_length=50) # 域名状态 1：急需续费。2：急需赎回。3：正常。
    ccompany = models.CharField(max_length=50)  # 域名持有人
    registration_date = models.DateTimeField()  # 注册时间
    expiration_date = models.DateTimeField()  # 到期时间
    expiration_curr_date_diff = models.IntegerField(default=0)  # 到期时间差
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)  # 关联的客户，并且如果该客户被删除，所有与之关联的云服务器实例也会被删除。

    def __str__(self):
        return self.domain_name  # 返回域名作为对象的字符串表示
