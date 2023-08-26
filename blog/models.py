from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    owner = models.ForeignKey(User, related_name='Owner', on_delete=models.CASCADE)
    authors = models.ManyToManyField(User, related_name='Authors')
    subscribers = models.ManyToManyField(User, related_name='Subscribers')

    def __str__(self):
        return self.title


class Tag(models.Model):
    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)

    likes = models.ManyToManyField(User, related_name='likes')
    views = models.PositiveIntegerField(default=0)

    # cat = models.ForeignKey('Category', on_delete=models.PROTECT, null=True)
    author = models.ForeignKey(User, related_name='PostAuthor', on_delete=models.CASCADE)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)

    tags = models.ManyToManyField(Tag, related_name='Tags')

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey('Post', on_delete=models.CASCADE, null=False)
    author = models.ForeignKey(User, related_name='CommentAuthor', on_delete=models.CASCADE)

    body = models.TextField(blank=False)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return (self.author, self.post)
