from rest_framework import serializers
from snapserver.models import User, Post, Comments, Profile


class PostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Post
        fields = ['url', 'id', 'title', 'upload', 'caption', 'date_posted', 'notes', 'author']
        # fields = '__all__'


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        lookup_field = 'email'
        # fields = '__all__'
        exclude = ('user_permissions',)
