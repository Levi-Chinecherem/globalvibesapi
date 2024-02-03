from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, UserDetails

# Register the models with the admin site using the decorator
@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    list_display = ['email', 'full_name', 'is_staff', 'is_superuser']
    search_fields = ['email', 'full_name']
    ordering = ['email']

@admin.register(UserDetails)
class UserDetailsAdmin(admin.ModelAdmin):
    list_display = ['user', 'full_name', 'address']
    search_fields = ['user__email', 'full_name']
    ordering = ['user__email']

# Customize the Django admin site header and title
admin.site.site_header = 'GlobalVibes Admin'
admin.site.site_title = 'GlobalVibes Administration'
