from django.urls import path
from rest_framework import routers
from . import views
from post.models import Post

router=routers.DefaultRouter()
router.register(r'Post',views.PostApiView)

urlpatterns = [
    path('',views.PostApiView.as_view(),name='post_api')
]
