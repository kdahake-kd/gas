
from django.db import models
from django.contrib.auth.models import User
from service_requests.models import ServiceRequest

class SupportInteraction(models.Model):
    service_request = models.ForeignKey(ServiceRequest, on_delete=models.CASCADE)
    support_rep = models.ForeignKey(User, on_delete=models.CASCADE)
    interaction_details = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Interaction for {self.service_request} by {self.support_rep.username}"
