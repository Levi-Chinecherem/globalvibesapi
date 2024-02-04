# chat/urls.py
from django.urls import path
from .views import CommunityMemberDetailsView, CommunityMemberListView, CommunityListView, CommunityJoinView, MuteCommunityView, SendMessageView, UserChatListView, NotificationListView, LeaveCommunityView

urlpatterns = [
    path('communities/', CommunityListView.as_view(), name='community-list'),
    path('join-community/', CommunityJoinView.as_view(), name='join-community'),
    path('send-message/<int:community_id>/', SendMessageView.as_view(), name='send-message'),
    path('chats/', UserChatListView.as_view(), name='user-chat-list'),
    path('notifications/', NotificationListView.as_view(), name='notification-list'),
    path('leave-community/<int:community_id>/', LeaveCommunityView.as_view(), name='leave-community'),
    path('mute-community/<int:community_id>/', MuteCommunityView.as_view(), name='mute-community'),
    path('community-members/', CommunityMemberListView.as_view(), name='community-member-list'),
    path('community-members/<int:pk>/', CommunityMemberDetailsView.as_view(), name='community-member-details'),
]
