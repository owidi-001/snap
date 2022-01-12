from rest_framework import serializers
from .models import Post, User, Following


class PostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Post
        # fields = '__all__'
        fields = ['id', 'url', 'upload', 'caption', 'author', 'date_posted']  # use with hyperlinked model
        # serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    # following = serializers.SerializerMethodField()
    # followers = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'phone', 'website', 'biography', 'avatar']

    # def get_following(self, obj):
    #     return FollowingSerializer(obj.following.all(), many=True).data
    #
    # def get_followers(self, obj):
    #     return FollowersSerializer(obj.followers.all(), many=True).data

    def create(self, validated_data):
        user = User.objects.create(**validated_data)
        return user


class FollowingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Following
        fields = ("id", "user", "follow")


class FollowersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Following
        fields = ("id", "user", "follow")
