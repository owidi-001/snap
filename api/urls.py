from django.urls import path

from .user_views import *
from .post_views import *

# Documentation
from rest_framework.documentation import include_docs_urls


urlpatterns = [
    # endpoints

    # users
    path('auth/register', RegisterView.as_view(), name='register'),
    path('auth/login', LoginView.as_view(), name='login'),
    path('auth/<int:pk>/', UserDetail.as_view(), name='user-detail'),

    # post
    path('post', PostList.as_view(),name="posts"),
    path('post/create', PostCreateView.as_view(),name="new_post"),
    path('post/<int:pk>/', PostDetail.as_view(), name='post-detail'),

    # passwords


    # Documentation
    path('', include_docs_urls(title="Snap")),
]

