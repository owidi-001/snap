from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from .serializers import FollowSerializer
from user.models import User

from user.serializers import UserSerializer

from .models import Follow


class FollowView(APIView):
    # TODO! Redo this
    def get_instance(self,request,pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise Http404

    def get(self,request):
        context={
            "followers":UserSerializer(Follow.objects.filter(user=request.user),many=True).data,
            "following":UserSerializer(Follow.objects.filter(follower=request.user),many=True).data
        }
        return Response(context,status=status.Http_200_OK)

    def post(self,request,pk):
        follower=User.objects.filter(pk=pk)[0]
        follow=self.get_instance(pk)

        serializer=FollowSerializer(follow)
        return Response(status=status.HTTP_201_CREATED)

    def patch(self,request,pk):
        user=self.get_instance(pk)




