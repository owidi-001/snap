from django.urls import path

from .user_views import *
from .post_views import *

# Documentation


urlpatterns = [
    # endpoints

    # users
    path('/register', RegisterView.as_view(), name='register'),
    path('/login', LoginView.as_view(), name='login'),
    path('/<int:pk>/', UserDetail.as_view(), name='user-detail'),

    # passwords
]

