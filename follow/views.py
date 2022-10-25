from django.shortcuts import render, get_object_or_404

# Create your views here.
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from follow.models import Follow
from follow.serializers import FollowSerializer
from user.models import User


class FollowView(APIView):
    permission_classes = []

    def get(self, request):
        followers = Follow.objects.filter(user=request.user)
        total_followers = followers.count()
        following = Follow.objects.filter(follow=request.user)
        total_following = following.count()

        serializer = FollowSerializer(followers, many=True)
        data = serializer.data
        data["followers_total"] = total_followers
        data["following_total"] = total_following

        return Response(data, status=status.HTTP_200_OK)

    def post(self, request):
        to_follow = get_object_or_404(User, id=request.to_follow)
        make_follow = Follow.objects.create(user=request.user, follow=to_follow)

        if make_follow:
            serializer = FollowSerializer(make_follow).data

            return Response({"message": f"You're now following {to_follow}"}, status=status.HTTP_201_CREATED)

    def put(self, request):
        to_follow = get_object_or_404(User, id=request.to_follow)

        is_follow = get_object_or_404(Follow, user=request.user, follow=to_follow)

        if is_follow:
            is_follow.delete()
            return Response({"message": f"Unfollowed {to_follow}"}, status=status.HTTP_201_CREATED)
        else:
            Follow.objects.create(user=request.user, follow=to_follow)
            return Response({"message": f"You're now following {to_follow}"}, status=status.HTTP_201_CREATED)
