from django.db.models import Count
from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response

from .models import Blog, Post
from .serializers import BlogSerializer, PostSerializer
from .permissions import IsAdminOrReadOny, IsOwnerOrReadOnly


# Create your views here.


class BlogAPIList(generics.ListCreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)


class BlogAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    permission_classes = (IsOwnerOrReadOnly,)


class BlogAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    permission_classes = (IsAdminOrReadOny,)


class PostsOfBlogAPIList(generics.ListCreateAPIView):
    serializer_class = PostSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get_queryset(self, id):
        return Post.objects.filter(
            blog=Blog.objects.get(id=id),
            is_published=True
        ).select_related('likes').annotate(
            Count('likes', distinct=True)
        )

    def list(self, request, *args, **kwargs):
        header = request.GET.get('header')
        posts = self.get_queryset(kwargs.get('id'))
        print(kwargs)

        return Response(status=200, data=self.serializer_class(PostSerializer, many=True).data)