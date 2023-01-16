from rest_framework import serializers

from .models import User

class UserSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'phone', 'website', 'biography', 'avatar']

    def create(self, validated_data):
        user = User.objects.create(**validated_data)
        return user
