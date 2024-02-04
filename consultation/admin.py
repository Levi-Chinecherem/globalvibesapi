# consultation/admin.py
from django.contrib import admin
from .models import Consultation, ConsultationNotification

@admin.register(Consultation)
class ConsultationAdmin(admin.ModelAdmin):
    list_display = ('sender', 'receiver', 'timestamp', 'admin_only')
    search_fields = ('sender__email', 'receiver__email', 'timestamp')
    list_filter = ('admin_only',)

@admin.register(ConsultationNotification)
class ConsultationNotificationAdmin(admin.ModelAdmin):
    list_display = ('user', 'consultation', 'unread_count', 'timestamp')
    search_fields = ('user__email', 'consultation__timestamp', 'unread_count')
