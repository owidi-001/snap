# Create your views here.
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from blog.models import Blog
from blog.schema import BlogSchema
from blog.serializers import BlogSerializer, BlogCreate


class BlogView(APIView):
    permission_classes = []
    schema = BlogSchema()

    def get(self, request):
        blogs = Blog.objects.filter(created_by=request.user)

        try:
            serializer = BlogSerializer(blogs, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            return Response({"message": "Failed to load blogs"}, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request):
        serializer = BlogCreate(data=request.data)

        if serializer.is_valid():
            blog = Blog.objects.create(created_by=request.user, upload=serializer.data.get("upload"),
                                       caption=serializer.data.get("caption"))

            serializer = BlogSerializer(blog)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)