from django.shortcuts import render, get_object_or_404

# Create your views here.
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from blog.models import Blog
from comment.models import Comment
from comment.schema import CommentSchema
from comment.serializers import CommentCreateSerializer, CommentSerializer


class CommentView(APIView):
    permission_classes = []
    schema = CommentSchema()

    # get
    def get(self, request):
        blog = get_object_or_404(Blog, id=request.blog)
        comments = Comment.objects.filter(blog=blog)
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
