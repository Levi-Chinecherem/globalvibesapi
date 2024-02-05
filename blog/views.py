# views.py

from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Category, BlogPost, Comment, Like, Favorite
from .serializers import CategorySerializer, BlogPostSerializer, CommentSerializer, LikeSerializer, FavoriteSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

# Category views

class CategoryListCreateView(generics.ListCreateAPIView):
    """
    View for listing and creating categories.
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

# BlogPost views

class BlogPostListCreateView(generics.ListCreateAPIView):
    """
    View for listing and creating blog posts.

    Supports search and filtering.
    """
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['categories', 'tags']  # Specify fields to filter
    search_fields = ['title', 'content', 'categories__name', 'tags__name']  # Specify fields to search

    def perform_create(self, serializer):
        # Automatically set the author of the blog post to the current user.
        serializer.save(author=self.request.user)

    def get_serializer(self, *args, **kwargs):
        # Handle file uploads for the cover image
        kwargs['context'] = self.get_serializer_context()
        return BlogPostSerializer(*args, **kwargs)

class BlogPostDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    View for retrieving, updating, and deleting a specific blog post.
    """
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer

# Comment views

class CommentListCreateView(generics.ListCreateAPIView):
    """
    View for listing and creating comments on blog posts.
    """
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        # Automatically set the author of the comment to the current user.
        serializer.save(author=self.request.user)

# Like and Favorite views

class LikeCreateView(generics.CreateAPIView):
    """
    View for creating a 'like' for a blog post.
    """
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    permission_classes = [IsAuthenticated]

class FavoriteCreateView(generics.CreateAPIView):
    """
    View for creating a 'favorite' for a blog post.
    """
    queryset = Favorite.objects.all()
    serializer_class = FavoriteSerializer
    permission_classes = [IsAuthenticated]
