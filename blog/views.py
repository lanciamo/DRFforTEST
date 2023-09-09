from django.db.models import Count
from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.response import Response

from .models import Blog, Post, Comment
from .serializers import *
from .permissions import *


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
    permission_classes = (IsAuthenticated,)

    # permission_classes = (IsAuthenticatedOrReadOnly,)

    def get_queryset(self):
        return Post.objects.filter(
            blog=Blog.objects.filter(
                id=self.request.parser_context.get('kwargs', {}).get('id')
            ).first(),
            is_published=True
        ).prefetch_related('likes').annotate(
            Count('likes', distinct=True))

    def list(self, request, *args, **kwargs):
        # header = request.GET.get('header')
        posts = self.get_queryset()
        print(kwargs)

        return Response(status=200, data=self.serializer_class(posts, many=True).data)


class PostAPICreate(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)


class PostAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsAuthorOrReadOnly,)


class PostAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsAdminOrReadOny,)


class CountLikesOfPost(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)


class LikeAPIAdd(generics.RetrieveUpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)


class LikeAPIRemove(generics.RetrieveUpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)


class TagsOfPostAPIList(generics.RetrieveDestroyAPIView):
    pass


class TagToPostAPICreate(generics.RetrieveDestroyAPIView):
    pass


class TagToPostAPIAdd(generics.RetrieveDestroyAPIView):
    pass


class TagsAPIList(generics.ListCreateAPIView):
    pass


class TagAPIUpdate(generics.RetrieveDestroyAPIView):
    pass


class TagAPIDelete(generics.RetrieveDestroyAPIView):
    pass


class CommentsListView(generics.ListCreateAPIView):
    serializer_class = BaseCommentSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get_queryset(self):
        return Comment.objects.filter(
            post=Post.objects.filter(
                id=self.request.parser_context.get('kwargs', {}).get('id')
            ).first(),
            parent__isnull=True
        )

    def list(self, request, *args, **kwargs):
        # header = request.GET.get('header')
        comments = self.get_queryset()
        print('Comment', kwargs)

        return Response(status=200, data=self.serializer_class(comments, many=True).data)


class CommentsTreeView(generics.RetrieveUpdateAPIView):
    queryset = Comment.objects.all()
    serializer_class = RecursiveCommentSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)


class CommentPostCreate(generics.ListCreateAPIView):
    queryset = Comment.objects.all()  # id=self.request.parser_context.get('kwargs', {}).get('id')
    serializer_class = CommentSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)


class CommentCommentCreate(generics.ListCreateAPIView):
    queryset = Comment.objects.all()  # id=self.request.parser_context.get('kwargs', {}).get('id')
    serializer_class = CommentSerializer
    permission_classes = (IsAuthenticated,)


class CommentAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = (IsAuthorOrReadOnly,)


class CommentAPIDelete(generics.RetrieveDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = (IsAuthorOrReadOnly,)
