# blog/models.py

from django.db import models
from django.conf import settings
from django.utils import timezone
from django.utils.text import slugify
from ckeditor_uploader.fields import RichTextUploadingField

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Tag"
        verbose_name_plural = "Tags"

class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=255, unique=True)
    cover_image = models.ImageField(upload_to='blog_covers/', null=True, blank=True)
    content = RichTextUploadingField()
    pub_date = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    categories = models.ManyToManyField(Category, related_name='blog_posts')
    tags = models.ManyToManyField(Tag, related_name='blog_posts')  # Updated related_name
    likes = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='liked_posts', blank=True)
    favorites = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='favorite_posts', blank=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-pub_date']

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

class Comment(models.Model):
    post = models.ForeignKey(BlogPost, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField()
    pub_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.author.username} - {self.post.title} - {self.content[:20]}"

    class Meta:
        ordering = ['-pub_date']
        
class Like(models.Model):
    post = models.ForeignKey(BlogPost, on_delete=models.CASCADE, related_name='post_likes')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username} likes {self.post.title}"

    class Meta:
        unique_together = ('user', 'post')

class Favorite(models.Model):
    post = models.ForeignKey(BlogPost, on_delete=models.CASCADE, related_name='post_favorites')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username} favorites {self.post.title}"

    class Meta:
        unique_together = ('user', 'post')
