# chat/models.py
from django.db import models
from accounts.models import CustomUser

User = CustomUser

class Community(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    cover_image = models.ImageField(upload_to='community_covers/', null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Community"
        verbose_name_plural = "Communities"

class CommunityMember(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    community = models.ForeignKey(Community, on_delete=models.CASCADE)
    joined_at = models.DateTimeField(auto_now_add=True)
    notification_muted = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username} in {self.community.name}"

    class Meta:
        verbose_name = "Community Member"
        verbose_name_plural = "Community Members"

class UserChat(models.Model):
    sender = models.ForeignKey(User, related_name='sent_chats', on_delete=models.CASCADE)
    community = models.ForeignKey(Community, on_delete=models.CASCADE)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.sender.username} in {self.community.name}"

    class Meta:
        verbose_name = "User Chat"
        verbose_name_plural = "User Chats"

class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    community = models.ForeignKey(Community, on_delete=models.CASCADE)
    unread_count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.user.username} in {self.community.name} - Unread: {self.unread_count}"

    class Meta:
        verbose_name = "Notification"
        verbose_name_plural = "Notifications"
