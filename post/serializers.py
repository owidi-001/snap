from rest_framework import serializers

from .models import Post


class PostSerializer(serializers.HyperlinkedModelSerializer):
    # comments = CommentSerializer()

    class Meta:
        model = Post
        fields = ['id', 'url', 'upload', 'caption', 'author', 'date_posted', 'comment']  # use with hyperlinked model
        