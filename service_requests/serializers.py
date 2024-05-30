from rest_framework import serializers
from .models import ServiceRequest
from django.contrib.auth.models import User

class ServiceRequestSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), required=False)

    class Meta:
        model = ServiceRequest
        fields = '__all__'
        read_only_fields = ['status', 'created_at', 'updated_at']

