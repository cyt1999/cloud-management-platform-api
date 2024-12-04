from rest_framework import serializers
from .models import Domain

class DomainSerializer(serializers.ModelSerializer):
    # 通过外键获取客户名称，read_only=True表示只读
    customer_name = serializers.CharField(source='customer.name', read_only=True)

    class Meta:
        model = Domain
        fields = ['id', 'domain_name', 'domain_status', 'ccompany', 'registration_date', 
                  'expiration_date', 'expiration_curr_date_diff', 'customer_name'] 