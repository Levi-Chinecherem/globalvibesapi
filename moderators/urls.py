# moderators/urls.py
from django.urls import path
from .views import ModeratorListView, PromoteToModeratorView

urlpatterns = [
    path('list/', ModeratorListView.as_view(), name='moderator-list'),
    path('promote/<int:user_id>/', PromoteToModeratorView.as_view(), name='promote-to-moderator'),
]
