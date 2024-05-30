
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SupportInteractionViewSet

router = DefaultRouter()
router.register(r'support_interactions', SupportInteractionViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
