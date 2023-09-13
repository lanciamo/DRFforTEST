from django.urls import path

from .views import *

urlpatterns = [
    # blogs
    path('blogs/', BlogsAPIListCreate.as_view()),  # list of blogs and create blog
    path('blog/<int:pk>/', BlogAPIRetrieveUpdateDestroy.as_view()),  # RetriveUpdateDelete

    # posts
    path('posts/', PostsAPIListCreate.as_view()),
    path('post/<int:pk>/', PostAPIRetrieveUpdateDestroy.as_view()),
    path('blog/<int:id>/posts/', PostsOfBlogAPIList.as_view()),
    path('post/<int:id>/tags/', PostTagsView.as_view()),
    path('post/<int:id>/likes/', PostLikesViewSet.as_view()),
    path('post/<int:id>/comments/', CommentsListView.as_view()),  # !!! list of comments to post w/o parents

    # tags
    path('tags/', TagsAPIListCreate.as_view()),
    path('tag/<int:pk>/', TagAPIRetrieveUpdateDestroy.as_view()),

    # comments
    path('comments/<int:pk>/tree/', CommentsTreeView.as_view()),  # !!! recursively list of comments to the comment
    path('comments/', CommentsAPIListCreate.as_view()),
    path('comment/<int:pk>/', CommentAPIRetrieveUpdateDestroy.as_view()),
]
