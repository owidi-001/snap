from django.urls import path, include
from django.contrib.auth import views as auth_views
# local views
from . import views

urlpatterns = [
    # post
    path('', views.home, name='home'),  # VIEW
    path('post_create', views.post_create, name='post_create'),  # CREATE

    # post detail
    path('<slug:post_slug>', views.post_detail, name='detail'),  # UPDATE & DELETE
    path('<int:pk>', views.post_comment, name='comment'),  # Comment

    # account
    path('', auth_views.LoginView.as_view(template_name='account/login.html'), name='login'),
    path('', auth_views.LogoutView.as_view(), name='logout'),
    path('profile', views.profile, name='profile'),

    # password management
    path('password_change/', auth_views.PasswordChangeView.as_view(), name='password_change'),
    path('password_change/done/ ', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),

]
