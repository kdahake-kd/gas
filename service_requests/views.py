
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import ServiceRequest
from .serializers import ServiceRequestSerializer
from django.contrib.auth.models import User


class ServiceRequestViewSet(viewsets.ModelViewSet):
    queryset = ServiceRequest.objects.all()
    serializer_class = ServiceRequestSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        if self.request.user.is_staff:
            return ServiceRequest.objects.all()
        return ServiceRequest.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        user = self.request.data.get('user')
        if user:
            user = User.objects.get(pk=user)
            serializer.save(user=user)
        else:
            serializer.save(user=self.request.user)

