from django.db import models

class Customer(models.Model):
    name = models.CharField(max_length=100)
    cloud_platform_type = models.CharField(max_length=100)
    account = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    access_key_id = models.CharField(max_length=100)
    access_key_secret = models.CharField(max_length=100)
    regions = models.JSONField()

    def __str__(self):
        return self.name 