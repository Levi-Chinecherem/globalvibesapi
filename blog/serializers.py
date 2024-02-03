# serializers.py

from rest_framework import serializers
from .models import Category, BlogPost, Comment, Like, Favorite

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = '__all__'

class FavoriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorite
        fields = '__all__'

class BlogPostSerializer(serializers.ModelSerializer):
    categories = CategorySerializer(many=True)
    comments = CommentSerializer(many=True)
    likes = LikeSerializer(many=True)
    favorites = FavoriteSerializer(many=True)

    class Meta:
        model = BlogPost
        fields = '__all__'
