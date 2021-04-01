from rest_framwork.views import viewsets
from rest_framwork.response import Response
from django.shortcuts import get_object_or_404
from .serializers import UserSerializer, PostSerializer
from snapserver.models import User, Post


class PostViewSet(viewsets.HyperLinkedModelViewSet):
    queryset = Post.objects.all().order_by('-date_posted')[:10]
    serializers_class = PostSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order
    serializers_class = UserSerializer
