from rest_framework import serializers
from post.models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        # fields = ['url','id','title','subtitle','upload','caption','date_posted','user']
        fields = ['id','title','subtitle','upload','caption','date_posted','user']