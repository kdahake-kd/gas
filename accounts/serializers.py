
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Profile
from service_requests.serializers import ServiceRequestSerializer

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    service_requests = ServiceRequestSerializer(many=True, read_only=True, source='user.servicerequest_set')

    class Meta:
        model = Profile
        fields = '__all__'
