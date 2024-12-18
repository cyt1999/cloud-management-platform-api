from django.db import models
from ..customer.models import Customer

class CloudServer(models.Model):
    instance_id = models.CharField(max_length=100)
    status = models.CharField(max_length=50)
    public_ip_address = models.GenericIPAddressField(null=True, blank=True)
    private_ip_address = models.GenericIPAddressField(null=True, blank=True)
    cpu = models.IntegerField(null=True, blank=True)
    memory = models.FloatField(null=True, blank=True)
    instance_charge_type = models.CharField(max_length=50, null=True, blank=True)
    creation_time = models.DateTimeField(null=True, blank=True)
    expired_time = models.DateTimeField(null=True, blank=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)

    def __str__(self):
        return self.instance_id

class MonitoringData(models.Model):
    cloud_server = models.ForeignKey(CloudServer, on_delete=models.CASCADE)
    cpu_usage = models.FloatField()
    disk_usage = models.FloatField()
    network_usage = models.FloatField()
    memory_usage = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Monitoring Data for {self.cloud_server.instance_id} at {self.timestamp}" 