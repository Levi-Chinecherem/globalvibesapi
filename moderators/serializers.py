# moderators/serializers.py
from rest_framework import serializers
from .models import Moderator, ModeratorNotification

class ModeratorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Moderator
        fields = '__all__'

class ModeratorNotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ModeratorNotification
        fields = '__all__'
        