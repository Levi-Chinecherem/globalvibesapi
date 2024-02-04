# moderators/admin.py
from django.contrib import admin
from .models import Moderator, ModeratorNotification

@admin.register(Moderator)
class ModeratorAdmin(admin.ModelAdmin):
    list_display = ('user',)

@admin.register(ModeratorNotification)
class ModeratorNotificationAdmin(admin.ModelAdmin):
    list_display = ('user', 'message', 'timestamp')
