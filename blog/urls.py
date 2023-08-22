from django.urls import path
from .views import *


urlpatterns = [
    path('', BlogAPIList.as_view()),
    path('<int:id>/posts/', PostsOfBlogAPIList.as_view()),
    ]