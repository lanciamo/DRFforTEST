from django.db.models import Count
from rest_framework import generics, mixins
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.response import Response

from .models import Blog, Post, Comment
from .serializers import *
from .permissions import *


# Create your views here.


class BlogsAPIListCreate(generics.ListCreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)


class BlogAPIRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    permission_classes = (IsOwnerOrReadOnly,)


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


class PostsAPIListCreate(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)


class PostAPIRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsAuthorOrReadOnly,)


class PostLikesViewSet(mixins.CreateModelMixin,
                       mixins.DestroyModelMixin,
                       generics.GenericAPIView):
    serializer_class = PostSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def post(self, request, *args, **kwargs):
        post = Post.objects.filter(id=kwargs.get('id')).first()
        post.likes.add(request.user)
        post.likes.save()

    def delete(self, request, *args, **kwargs):
        post = Post.objects.filter(id=kwargs.get('id')).first()
        post.likes.remove(request.user)
        post.likes.save()


class PostTagsView(mixins.CreateModelMixin,
                   mixins.UpdateModelMixin,
                   generics.GenericAPIView):
    serializer_class = PostSerializer

    def post(self, request, *args, **kwargs):
        post = Post.objects.filter(id=kwargs.get('id')).first()
        post.tags = Tags.objects.filter(id__in=request.POST.get('ids'))
        post.tags.save()


class TagsAPIListCreate(generics.ListCreateAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class TagAPIRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


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


class CommentsAPIListCreate(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)


class CommentAPIRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = (IsAuthorOrReadOnly,)
