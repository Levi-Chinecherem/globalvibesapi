# moderators/urls.py
from django.urls import path
from .views import ModeratorListView, PromoteToModeratorView, DemoteFromModeratorView

urlpatterns = [
    path('list/', ModeratorListView.as_view(), name='moderator-list'),
    path('promote/<int:user_id>/', PromoteToModeratorView.as_view(), name='promote-to-moderator'),
    path('demote/<int:user_id>/', DemoteFromModeratorView.as_view(), name='demote-from-moderator'),  # Add this URL
]
