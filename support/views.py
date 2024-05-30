

from rest_framework import viewsets
from .models import SupportInteraction
from .serializers import SupportInteractionSerializer

class SupportInteractionViewSet(viewsets.ModelViewSet):
    queryset = SupportInteraction.objects.all()
    serializer_class = SupportInteractionSerializer

