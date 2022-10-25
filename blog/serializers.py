from rest_framework import serializers

from blog.models import Blog
from comment.serializers import CommentSerializer


class BlogSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True)

    class Meta:
        model = Blog
        fields = ["id", "created_by", "upload", "slug", "caption", "date_posted", "comments"]


class BlogCreate(serializers.Serializer):
    upload = serializers.FileField()
    caption = serializers.CharField()
