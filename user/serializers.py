from rest_framework import serializers

from .models import User

class UserSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'phone', 'website', 'biography', 'avatar']

    def create(self, validated_data):
        user = User.objects.create(**validated_data)
        return user

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["email", ]


class PasswordSerializer(serializers.Serializer):
    """
    Serializer for password reset endpoint.
    """
    email = serializers.EmailField(required=True)


class NewPasswordSerializer(serializers.Serializer):
    uid = serializers.CharField()
    new_password = serializers.CharField()
    short_code = serializers.IntegerField()
