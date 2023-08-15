from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    owner = models.ForeignKey(User, verbose_name='Owner', on_delete=models.CASCADE)
    authors = models.ManyToManyField(User, verbose_name='Authors', on_delete=models.PROTECT)
    subscribers = models.ManyToManyField(User, verbose_name='Subscribers', on_delete=models.PROTECT)

    tags = models.ManyToManyField(Tag, verbose_name='Authors', on_delete=models.PROTECT)

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

    likes = models.ManyToManyField(User, verbose_name='Likers', on_delete=models.PROTECT)
    views = models.PositiveIntegerField(default=0)

    # cat = models.ForeignKey('Category', on_delete=models.PROTECT, null=True)
    author = models.ForeignKey(User, verbose_name='Author', on_delete=models.CASCADE)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)

    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey('Post', on_delete=models.CASCADE, null=False)
    author = models.ForeignKey(User, verbose_name='Author', on_delete=models.CASCADE)

    body = models.TextField(blank=False)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return (self.author, self.post)
