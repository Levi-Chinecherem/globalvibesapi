# chat/admin.py
from django.contrib import admin
from .models import Community, CommunityMember, UserChat, Notification

@admin.register(Community)
class CommunityAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'creator', 'cover_image')
    search_fields = ('name', 'creator__username')

@admin.register(CommunityMember)
class CommunityMemberAdmin(admin.ModelAdmin):
    list_display = ('user', 'community')
    search_fields = ('user__username', 'community__name')

@admin.register(UserChat)
class UserChatAdmin(admin.ModelAdmin):
    list_display = ('sender', 'community', 'message', 'timestamp')
    search_fields = ('sender__username', 'community__name', 'message')

@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ('user', 'community', 'unread_count')
    search_fields = ('user__username', 'community__name')
