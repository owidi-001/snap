from post.models import Post
from rest_framework import generics
from .serializers import PostSerializer

class PostApiView(generics.ListAPIView):
    queryset=Post.objects.all()
    serializer_class=PostSerializer

# class PostApiView(generics.DetailView):
#     queryset=Post.objects.all()
#     serializer_claass=PostSerializer
