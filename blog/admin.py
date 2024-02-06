# blog/admin.py

from django.contrib import admin
from .models import Category, Tag, BlogPost, Comment, Like, Favorite

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'pub_date',)
    search_fields = ('title', 'author__username',)
    filter_horizontal = ['categories']
    date_hierarchy = 'pub_date'
    prepopulated_fields = {'slug': ('title',)}

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'post', 'pub_date',)
    search_fields = ('author__username', 'post__title',)
    date_hierarchy = 'pub_date'

@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ('user', 'post',)

@admin.register(Favorite)
class FavoriteAdmin(admin.ModelAdmin):
    list_display = ('user', 'post',)
