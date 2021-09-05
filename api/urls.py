from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    # posts
    path('post/', views.PostList.as_view()),
    path('api/<int:pk>/', views.PostDetail.as_view(), name='post-detail'),

    # users
    path('user/', views.UserListView.as_view()),
    path('user/<int:pk>/', views.UserDetail.as_view(), name='profile'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
