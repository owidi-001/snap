from django.urls import path, include
from .views import register, logout, profile, home, post_create, post_view  # login
# auth and password
from django.contrib.auth import views as auth_views

urlpatterns = [
    # blog api
    path('api', include('snapserver.api.urls')),

    # accounts
    path('auth', register, name='register'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', logout, name='logout'),
    path('profile', profile, name='profile'),

    # password management
    path('password_change/', auth_views.PasswordChangeView.as_view(), name='password_change'),
    path('password_change/done/ ', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),

    # post
    path('', home, name='home'),
    path('post_create', post_create, name='post_create'),

    # test post display
    path('post', post_view, name='posts'),

]
