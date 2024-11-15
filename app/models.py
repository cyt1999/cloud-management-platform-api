from django.db import models

# 客户管理表
class Customer(models.Model):
    name = models.CharField(max_length=100)
    cloud_platform_type = models.CharField(max_length=100)
    account = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    key = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# 云服务器信息表
class CloudServer(models.Model):
    instance_name = models.CharField(max_length=100)
    instance_id = models.CharField(max_length=100)
    status = models.CharField(max_length=50)
    specification = models.CharField(max_length=100)
    ip_address = models.GenericIPAddressField()
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)

    def __str__(self):
        return self.instance_name

# 监控数据表
class MonitoringData(models.Model):
    cloud_server = models.ForeignKey(CloudServer, on_delete=models.CASCADE)
    cpu_usage = models.FloatField()
    disk_usage = models.FloatField()
    network_usage = models.FloatField()
    memory_usage = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Monitoring Data for {self.cloud_server.instance_name} at {self.timestamp}"

# 域名表
class Domain(models.Model):
    domain_name = models.CharField(max_length=100)
    domain_status = models.CharField(max_length=50)
    real_name_auth_status = models.CharField(max_length=50)
    registration_date = models.DateTimeField()
    expiration_date = models.DateTimeField()

    def __str__(self):
        return self.domain_name 