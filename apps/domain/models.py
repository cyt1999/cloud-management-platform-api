from django.db import models
from ..customer.models import Customer

class Domain(models.Model):
    domain_name = models.CharField(max_length=100)
    domain_status = models.CharField(max_length=50)
    ccompany = models.CharField(max_length=50)
    registration_date = models.DateTimeField()
    expiration_date = models.DateTimeField()
    expiration_curr_date_diff = models.IntegerField(default=0)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)

    def __str__(self):
        return self.domain_name 