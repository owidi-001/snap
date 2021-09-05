from rest_framework import serializers
from .models import Post, User


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'
        # fields = ['id', 'url', 'title', 'upload', 'caption', 'author', 'date_posted'] # use with hyperlinked model
        # serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'phone', 'website', 'biography', 'avatar']

    def create(self, validated_data):
        user = User.objects.create(**validated_data)
        return user
