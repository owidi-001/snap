from rest_framework import serializers

from comment.models import Comment


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        field = ["__all__"]


class CommentCreateSerializer(serializers.Serializer):
    message = serializers.CharField(max_length=500)
