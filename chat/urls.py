# chat/urls.py
from django.urls import path
from .views import (
    CommunityListView,
    CommunityJoinView,
    CommunityMemberListView,
    CommunityMemberDetailsView,
    LeaveCommunityView,
    SendMessageView,
    UserChatListView,
    NotificationListView,
    MuteCommunityView,
    UserCommunitiesListView,  # Add this import
)

urlpatterns = [
    path('communities/', CommunityListView.as_view(), name='community-list'),
    path('communities/join/', CommunityJoinView.as_view(), name='community-join'),
    path('communities/members/', CommunityMemberListView.as_view(), name='community-member-list'),
    path('communities/members/<int:pk>/', CommunityMemberDetailsView.as_view(), name='community-member-details'),
    path('communities/leave/<int:community_id>/', LeaveCommunityView.as_view(), name='leave-community'),
    path('communities/<int:community_id>/send/', SendMessageView.as_view(), name='send-message'),
    path('communities/<int:community_id>/chats/', UserChatListView.as_view(), name='user-chat-list'),
    path('notifications/', NotificationListView.as_view(), name='notification-list'),
    path('communities/<int:community_id>/mute/', MuteCommunityView.as_view(), name='mute-community'),
    path('communities/user/', UserCommunitiesListView.as_view(), name='user-communities-list'),  # Add this URL
]
