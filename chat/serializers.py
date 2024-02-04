# chat/serializers.py
from rest_framework import serializers
from .models import Community, CommunityMember, UserChat, Notification
from accounts.serializers import UserDetailsSerializer
from accounts.models import CustomUser

User = CustomUser

class CommunitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Community
        fields = '__all__'

class CommunityMemberSerializer(serializers.ModelSerializer):
    username = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = CommunityMember
        fields = ['username', 'community', 'joined_at', 'notification_muted']


class UserChatSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserChat
        fields = '__all__'

class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = '__all__'

class CommunityMemberDetailsSerializer(serializers.ModelSerializer):
    user_details = UserDetailsSerializer(source='user.userdetails', read_only=True)

    class Meta:
        model = CommunityMember
        fields = ['user', 'joined_at', 'notification_muted', 'user_details']
