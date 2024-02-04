# moderators/models.py
from django.db import models
from accounts.models import CustomUser
from django.utils import timezone

class Moderator(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.email} - Moderator"

class ModeratorNotification(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    message = models.TextField()
    timestamp = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.user.email} - Moderator Notification"

    class Meta:
        verbose_name = "Moderator Notification"
        verbose_name_plural = "Moderator Notifications"
