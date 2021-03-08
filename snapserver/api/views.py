from rest_framwork.views import viewsets
from rest_framwork.response import Response
from django.shortcuts import get_object_or_404
from .serializers import UserSerializer,PostSerializer
from snapserver.models import User,Post

class PostViewSet(viewsets.ModelViewSet):
    queryset=Post.objects.all()
    serializers_class=PostSerializer


# class PostViewSet(viewsets.ViewSet):
#     """
#     A simple ViewSet for listing or retrieving users.
#     """
#     def list(self,request):
#         queryset=Post.objects.all().order('-date_posted')
#         serializers_class=PostSerializer(queryset,many=True)
#         return Response(serializer.data)
    
#     def retrive(self,request,pk=None):
#         queryset=Post.objects.all()
#         user=get_object_or_404(queryset,pk=pk)
#         serializers_class=PostSerializer(user)
#         return Response(serializer.data)


class UserViewSet(viewsets.ModelViewSet):
    queryset=User.objects.all().order
    serializers_class=UserSerializer