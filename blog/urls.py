from django.urls import path
from .views import *


urlpatterns = [
    path('', BlogAPIList.as_view()),
    path('<int:id>/posts/', PostsOfBlogAPIList.as_view()),
    path('post/<int:pk>/', PostAPIRead.as_view()),
    path('post_update/<int:pk>/', PostAPIUpdate.as_view()),
    path('post_delete/<int:pk>/', PostAPIDestroy.as_view()),
    ]