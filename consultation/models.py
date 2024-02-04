# consultation/models.py
from django.db import models
from accounts.models import CustomUser
from django.utils import timezone

class Consultation(models.Model):
    sender = models.ForeignKey(CustomUser, related_name='sent_consultations', on_delete=models.CASCADE)
    receiver = models.ForeignKey(CustomUser, related_name='received_consultations', on_delete=models.CASCADE)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    admin_only = models.BooleanField(default=False)  # New field to indicate admin-only consultations

    def __str__(self):
        return f"Consultation between {self.sender.email} and {self.receiver.email}"

class ConsultationNotification(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    consultation = models.ForeignKey(Consultation, on_delete=models.CASCADE)
    unread_count = models.PositiveIntegerField(default=0)
    timestamp = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.user.email} in consultation - Unread: {self.unread_count}"

    class Meta:
        verbose_name = "Consultation Notification"
        verbose_name_plural = "Consultation Notifications"
