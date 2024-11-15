from django.db import models
from CustomerApp.models import Customer

# 云服务器模型，存储云服务器的基本信息
class CloudServer(models.Model):
    instance_name = models.CharField(max_length=100)  # 实例名称
    instance_id = models.CharField(max_length=100)  # 实例ID
    status = models.CharField(max_length=50)  # 状态
    specification = models.CharField(max_length=100)  # 规格
    ip_address = models.GenericIPAddressField()  # IP地址
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)  # 关联的客户

    def __str__(self):
        return self.instance_name  # 返回实例名称作为对象的字符串表示

# 监控数据模型，存储云服务器的监控信息
class MonitoringData(models.Model):
    cloud_server = models.ForeignKey(CloudServer, on_delete=models.CASCADE)  # 关联的云服务器
    cpu_usage = models.FloatField()  # CPU使用率
    disk_usage = models.FloatField()  # 磁盘使用率
    network_usage = models.FloatField()  # 网络使用率
    memory_usage = models.FloatField()  # 内存使用率
    timestamp = models.DateTimeField(auto_now_add=True)  # 数据记录时间

    def __str__(self):
        return f"Monitoring Data for {self.cloud_server.instance_name} at {self.timestamp}"  # 返回监控数据的字符串表示
