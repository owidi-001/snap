from django.urls import path

from .user_views import *
from .post_views import *

# Documentation
from rest_framework.documentation import include_docs_urls


urlpatterns = [
    # endpoints
    # post
    path('post', PostList.as_view()),
    path('post/<int:pk>/', PostDetail.as_view(), name='post-detail'),

    # users
    path('user/<int:pk>/', UserDetail.as_view(), name='user-detail'),
    path('auth/register', RegisterView.as_view(), name='register'),
    path('auth/login', LoginView.as_view(), name='login'),

    # passwords

    # Documentation
    path('', include_docs_urls(title="Snap")),
]

