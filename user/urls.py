from django.urls import path

# Documentation
from rest_framework.documentation import include_docs_urls

from .views import RegisterView, LoginView, UpdateUserView, ResetPasswordView

urlpatterns = [
    # endpoints

    # users
    path('', RegisterView.as_view(), name='register'),
    # path('auth/register', RegisterView.as_view(), name='register'), # Use when landing page is complete
    path('auth/login', LoginView.as_view(), name='login'),
    path('auth/update', UpdateUserView.as_view(), name='user_update'),
    path('auth/reset', ResetPasswordView.as_view(), name='reset_password'),


    # passwords


    # Documentation
    path('', include_docs_urls(title="Snap")),
]

