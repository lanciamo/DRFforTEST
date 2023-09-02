from django.urls import path, include, re_path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

from .views import *


urlpatterns = [
    path('', BlogAPIList.as_view()),
    path('drf-auth/', include('rest_framework.urls')),
    path('auth/', include('djoser.urls')),  # https://djoser.readthedocs.io/en/latest/base_endpoints.html
    re_path(r'^auth/', include('djoser.urls.authtoken')),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    #blogs
    path('list/', BlogAPIList.as_view()),
    path('create/', BlogAPIList.as_view()),
    path('update/', BlogAPIUpdate.as_view()),
    path('delete/', BlogAPIDestroy.as_view()),
    path('<int:id>/posts/', PostsOfBlogAPIList.as_view()),
    #posts
    path('post_create/', PostAPICreate.as_view()), # we need to make view to create!!! and insert blog id to add post
    path('post_update/<int:pk>/', PostAPIUpdate.as_view()), # read and update post
    path('post_delete/<int:pk>/', PostAPIDestroy.as_view()), # read and delete
    ]
