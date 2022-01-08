from . import views
from django.urls import path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
# Documentation
from rest_framework import permissions

schema_view = get_schema_view(
   openapi.Info(
      title="Snap API",
      default_version='v1',
      description=" ",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snap.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    # documentation routes
    path("api/", schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path("redocs/", schema_view.with_ui("redoc", cache_timeout=0), name='schema-redoc'),

    # endpoints
    path('post_list', views.PostList.as_view()),
    path('post_detail/<int:pk>/', views.PostDetail.as_view(), name='post-detail'),

    # users
    path('user/', views.UserListView.as_view()),
    path('user/<int:pk>/', views.UserDetail.as_view(), name='profile'),
]

