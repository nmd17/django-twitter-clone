from django.db import models
from userProfile.models import Profile

# Create your models here.

class Notification(models.Model):
    sender = models.ForeignKey(Profile, on_delete=models.CASCADE)
    recipient = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='recipient_notification')
    message = models.TextField()
    read = models.BooleanField(default=False)
    sent_date = models.DateTimeField(auto_now_add=True)