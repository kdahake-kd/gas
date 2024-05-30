
from rest_framework import serializers
from .models import SupportInteraction

class SupportInteractionSerializer(serializers.ModelSerializer):
    class Meta:
        model = SupportInteraction
        fields = '__all__'
