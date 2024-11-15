from rest_framework import serializers
from .models import CloudServer, MonitoringData

class CloudServerSerializer(serializers.ModelSerializer):
    class Meta:
        model = CloudServer
        fields = '__all__'

class MonitoringDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = MonitoringData
        fields = '__all__' 