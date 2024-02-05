# chat/views.py
from rest_framework import generics, status
from rest_framework import permissions
from .models import Community, UserChat, Notification, CommunityMember
from .serializers import CommunitySerializer, UserChatSerializer, NotificationSerializer, CommunityMemberSerializer, CommunityMemberDetailsSerializer
from rest_framework.decorators import permission_classes
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

from accounts.models import CustomUser

User = CustomUser

class CommunityListView(generics.ListAPIView):
    """
    View to list all communities.

    Publicly accessible to any user.
    """
    queryset = Community.objects.all()
    serializer_class = CommunitySerializer
    permission_classes = [permissions.AllowAny]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['name']  # Specify fields to filter
    search_fields = ['name', 'description']  # Specify fields to search

class UserCommunitiesListView(generics.ListAPIView):
    """
    View to list communities that a user belongs to.

    Requires authentication. Users can see the communities they belong to.
    """
    serializer_class = CommunitySerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Retrieve the user's community memberships
        user_communities = CommunityMember.objects.filter(user=self.request.user)
        return [membership.community for membership in user_communities]

class CommunityJoinView(generics.CreateAPIView):
    """
    View to allow a user to join a community.

    Requires authentication. Users can join communities.
    """
    queryset = CommunityMember.objects.all()
    serializer_class = CommunityMemberSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class CommunityMemberListView(generics.ListAPIView):
    """
    View to list members of a community.

    Requires authentication. Users can see the members of a community.
    """
    queryset = CommunityMember.objects.all()
    serializer_class = CommunityMemberSerializer
    permission_classes = [permissions.IsAuthenticated]

class CommunityMemberDetailsView(generics.RetrieveAPIView):
    """
    View to retrieve details of a community member.

    Requires authentication. Users can see the details of a community member.
    """
    queryset = CommunityMember.objects.all()
    serializer_class = CommunityMemberDetailsSerializer
    permission_classes = [permissions.IsAuthenticated]

class LeaveCommunityView(generics.DestroyAPIView):
    """
    View to allow a user to leave a community.

    Requires authentication. Users can leave communities.
    """
    queryset = CommunityMember.objects.all()
    serializer_class = CommunityMemberSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        community_id = self.kwargs['community_id']
        community = get_object_or_404(Community, pk=community_id)
        return get_object_or_404(CommunityMember, user=self.request.user, community=community)

    def perform_destroy(self, instance):
        instance.delete()

@permission_classes([permissions.IsAuthenticated])
class SendMessageView(generics.CreateAPIView):
    """
    View to send a message in a community.

    Requires authentication. Users can send messages in communities.
    """
    serializer_class = UserChatSerializer

    def perform_create(self, serializer):
        community_id = self.kwargs['community_id']
        community = get_object_or_404(Community, pk=community_id)
        sender = self.request.user
        serializer.save(sender=sender, community=community)

        # Notify other community members about the new message
        community_members = CommunityMember.objects.filter(community=community)
        for member in community_members:
            if member.user != sender:
                notification, created = Notification.objects.get_or_create(user=member.user, community=community)
                notification.unread_count += 1
                notification.save()

class UserChatListView(generics.ListCreateAPIView):
    """
    View to list and create user chats in communities.

    Requires authentication. Users can list and create user chats in communities.
    """
    queryset = UserChat.objects.all()
    serializer_class = UserChatSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return UserChat.objects.filter(community__members=self.request.user)

class NotificationListView(generics.ListAPIView):
    """
    View to list notifications for a user.

    Requires authentication. Users can see their notifications.
    """
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Notification.objects.filter(user=self.request.user)

class MuteCommunityView(generics.UpdateAPIView):
    """
    View to mute/unmute community notifications for a user.

    Requires authentication. Users can mute/unmute community notifications.
    """
    serializer_class = CommunityMemberSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        community_id = self.kwargs['community_id']
        community = get_object_or_404(Community, pk=community_id)
        return get_object_or_404(CommunityMember, user=self.request.user, community=community)

    def perform_update(self, serializer):
        instance = serializer.save(notification_muted=not serializer.instance.notification_muted)

        # Create a notification to inform the user about the mute/unmute action
        action_message = "muted" if instance.notification_muted else "unmuted"
        notification_message = f"You have {action_message} community messages notifications."
        Notification.objects.create(user=self.request.user, community=instance.community, message=notification_message)

        # Return appropriate success message along with the notification status
        success_message = f"Community messages notifications successfully {action_message}."
        return Response({"notification_muted": instance.notification_muted, "message": success_message}, status=status.HTTP_200_OK)
