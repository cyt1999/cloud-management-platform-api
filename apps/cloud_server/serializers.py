from rest_framework import serializers
from .models import CloudServer, MonitoringData

class CloudServerSerializer(serializers.ModelSerializer):
    customer_name = serializers.CharField(source='customer.name', read_only=True)

    class Meta:
        model = CloudServer
        fields = ['id', 'instance_id', 'status', 'public_ip_address', 'private_ip_address', 
                 'cpu', 'memory', 'instance_charge_type', 'creation_time', 'expired_time', 'customer_name']

class MonitoringDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = MonitoringData
        fields = '__all__' 