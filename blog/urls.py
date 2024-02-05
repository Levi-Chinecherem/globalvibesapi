# urls.py

from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import (
    CategoryListCreateView,
    BlogPostListCreateView,
    BlogPostDetailView,
    CommentListCreateView,
    LikeCreateView,
    FavoriteCreateView,
)

urlpatterns = [
    # Category URLs
    path('categories/', CategoryListCreateView.as_view(), name='category-list-create'),

    # BlogPost URLs
    path('blogposts/', BlogPostListCreateView.as_view(), name='blogpost-list-create'),
    path('blogposts/<int:pk>/', BlogPostDetailView.as_view(), name='blogpost-detail'),

    # Comment URLs
    path('comments/', CommentListCreateView.as_view(), name='comment-list-create'),

    # Like and Favorite URLs
    path('likes/', LikeCreateView.as_view(), name='like-create'),
    path('favorites/', FavoriteCreateView.as_view(), name='favorite-create'),
]

# Apply format suffix patterns for URL patterns
urlpatterns = format_suffix_patterns(urlpatterns)
