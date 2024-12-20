from rest_framework import serializers
from .models import Customer

class CustomerCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields ='__all__'  

class CustomerRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields =   ['id','name','cloud_platform_type','account','password']# 查询时不返回 AccessKey ID 和 AccessKey Secret
