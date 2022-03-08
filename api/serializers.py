from rest_framework import serializers
from .models import Post, User, Following, Comment


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["email", ]


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        field = ["__all__"]


class PostSerializer(serializers.HyperlinkedModelSerializer):
    comments = CommentSerializer()

    class Meta:
        model = Post
        # fields = '__all__'
        fields = ['id', 'url', 'upload', 'caption', 'author', 'date_posted', 'comment']  # use with hyperlinked model
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


class PasswordSerializer(serializers.Serializer):
    """
    Serializer for password reset endpoint.
    """
    email = serializers.EmailField(required=True)


class NewPasswordSerializer(serializers.Serializer):
    uid = serializers.CharField()
    new_password = serializers.CharField()
    short_code = serializers.IntegerField()

class FollowingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Following
        fields = ("id", "user", "follow")


class FollowersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Following
        fields = ("id", "user", "follow")
