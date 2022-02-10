from django.urls import path

# from . import views
from .user_views import *
from .post_views import *
# Documentation

# Documentation
from rest_framework.documentation import include_docs_urls


urlpatterns = [
    # endpoints
    path('post', PostList.as_view()),
    path('post/<int:pk>/', PostDetail.as_view(), name='post-detail'),

    # users
    path('user/', UserListView.as_view()),
    path('user/<int:pk>/', UserDetail.as_view(), name='user-detail'),

    # Documentation
    path('', include_docs_urls(title="Snap")),
]

