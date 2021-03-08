from rest_framework import serializers
from snapserver.models import User,Post,Comments,Profile

class PostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Post
        fields='__all__'

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=User
        fields='__all__'
