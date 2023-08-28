from django.urls import path, include
from .views import *


urlpatterns = [
    path('', BlogAPIList.as_view()),
    path('drf-auth/', include('rest_framework.urls')),
    path('<int:id>/posts/', PostsOfBlogAPIList.as_view()),
    path('post_create/', PostAPICreate.as_view()), # we need to make view to create!!!
    path('post_update/<int:pk>/', PostAPIUpdate.as_view()), # read and update post
    path('post_delete/<int:pk>/', PostAPIDestroy.as_view()), # read and delete
    ]