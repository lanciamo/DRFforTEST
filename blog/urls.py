from django.urls import path

from .views import *

urlpatterns = [
    # blogs
    path('blogs/', BlogAPIList.as_view()),
    path('blog_create/', BlogAPIList.as_view()),
    path('blog_update/<int:pk>/', BlogAPIUpdate.as_view()),
    path('blog_delete/<int:pk>/', BlogAPIDestroy.as_view()),

    path('blog/<int:id>/posts/', PostsOfBlogAPIList.as_view()),

    # posts
    path('post_create/', PostAPICreate.as_view()),  # we need to make view to create!!! and insert blog id to add post
    path('post_update/<int:pk>/', PostAPIUpdate.as_view()),  # read and update post
    path('post_delete/<int:pk>/', PostAPIDestroy.as_view()),  # read and delete

    # likes
    path('post_likes_count/<int:pk>/', CountLikesOfPost.as_view()),  # !!! list of likes to post
    path('post_like_create/<int:pk>/', LikeAPIAdd.as_view()),  # create like from this user to this post
    path('post_like_delete/<int:pk>/', LikeAPIRemove.as_view()),  # delete like from this user to this post

    # tags
    path('post/<int:id>/tags/', TagsOfPostAPIList.as_view()),  # !!! list of tags to post
    path('post/<int:id>/tag_create_and_add/', TagToPostAPICreate.as_view()),  # create global and add to this post
    path('post/<int:id>/tags_add/<int:pk>', TagToPostAPIAdd.as_view()),  # add existing tag to this post
    path('tag_list_or_create/', TagsAPIList.as_view()),  # list of existing or create global tag
    path('tag_update/<int:pk>/', TagAPIUpdate.as_view()),  # update tag
    path('tag_delete/<int:id>/', TagAPIDelete.as_view()),  # delete tag

    # comments
    path('post/<int:id>/comments/', CommentsListView.as_view()),  # !!! list of comments to post w/o parents
    path('comments/<int:pk>/tree/', CommentsTreeView.as_view()),  # !!! recursively list of comments to the comment
    path('post/<int:id>/post_comments_create/', CommentPostCreate.as_view()),
    path('comments/<int:pk>/comment_comment_create/', CommentCommentCreate.as_view()),
    path('comment_update/<int:pk>/', CommentAPIUpdate.as_view()),  # update global
    path('comment_delete/<int:pk>/', CommentAPIDelete.as_view()),  # update global

]
