from django.urls import path

from .views import *

urlpatterns = [
    # blogs
    path('blogs/', BlogsAPIListCreate.as_view()),
    path('blog/<int:pk>/', BlogAPIRetrieveUpdateDestroy.as_view()),

    # posts
    path('posts/', PostsAPIListCreate.as_view()),
    path('post/<int:pk>/', PostAPIRetrieveUpdateDestroy.as_view()),
    path('blog/<int:id>/posts/', PostsOfBlogAPIList.as_view()),
    path('post/<int:id>/tags/', PostTagsView.as_view()),
    path('post/<int:id>/likes/', PostLikesViewSet.as_view()),
    path('post/<int:id>/comments/', CommentsListView.as_view()),

    # tags
    path('tags/', TagsAPIListCreate.as_view()),
    path('tag/<int:pk>/', TagAPIRetrieveUpdateDestroy.as_view()),

    # comments
    path('comments/<int:pk>/tree/', CommentsTreeView.as_view()),
    path('comments/', CommentsAPIListCreate.as_view()),
    path('comment/<int:pk>/', CommentAPIRetrieveUpdateDestroy.as_view()),
]
