
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/accounts/', include('accounts.urls')),
    path('api/requests/', include('service_requests.urls')),
    path('api/support/', include('support.urls')),
    path('api-auth/', include('rest_framework.urls')),
]
