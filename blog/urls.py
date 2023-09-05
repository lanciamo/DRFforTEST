from django.urls import path

from .views import *

urlpatterns = [
    # blogs
    path('blogs/', BlogAPIList.as_view()),
    path('blog_create/', BlogAPIList.as_view()),
    path('blog_update/<int:id>/', BlogAPIUpdate.as_view()),
    path('blog_delete/<int:id>/', BlogAPIDestroy.as_view()),

    path('blog/<int:id>/posts/', PostsOfBlogAPIList.as_view()),

    # posts
    path('post_create/', PostAPICreate.as_view()),  # we need to make view to create!!! and insert blog id to add post
    path('post_update/<int:pk>/', PostAPIUpdate.as_view()),  # read and update post
    path('post_delete/<int:pk>/', PostAPIDestroy.as_view()),  # read and delete

    # likes
    path('post/<int:id>/likes/', PostsOfBlogAPIList.as_view()),  # !!! list of likes to post
    path('post/<int:id>/like_create/', PostsOfBlogAPIList.as_view()),  # create like from this user to this post
    path('post/<int:id>/like_delete/', PostsOfBlogAPIList.as_view()),  # delete like from this user to this post

    # tags
    path('post/<int:id>/tags/', PostsOfBlogAPIList.as_view()),  # !!! list of tags to post
    path('post/<int:id>/tag_create_and_add/', PostsOfBlogAPIList.as_view()),  # create global and add to this post
    path('post/<int:id>/tags_add/', PostsOfBlogAPIList.as_view()),  # add existing tag to this post
    path('tag_create/', PostsOfBlogAPIList.as_view()),  # create global tag
    path('tag_update/<int:pk>/', PostsOfBlogAPIList.as_view()),  # update tag
    path('tag_delete/<int:id>/', PostsOfBlogAPIList.as_view()),  # delete tag

    # comments
    path('post/<int:id>/comments/', CommentsListView.as_view()),  # !!! list of comments to post w/o parents
    path('comments/<int:pk>/tree/', CommentsTreeView.as_view()),  # !!! recursively list of comments to the comment
    # create comment on that entity, that I stay: or the Post, or the Comment
    # update global
    # delete global
]
