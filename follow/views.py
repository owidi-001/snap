from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView



from .serializers import FollowSerializer

from .models import Follow

# Create your views here.
class FollowView(APIView):
    def get(self,request):
        user=request.user
        followers=Follow.objects.filter(followed=user)

        serializer=FollowSerializer(followers,many=True)

        return Response(serializer.data,status=status.HTTP_200_OK)

    def post(self,request):
        user=request.user
        # Get user to follow

        # Create new follow

    def delete(self):
        user=request.user

        # Get user follow instance

        # if follow instance exists, remove
        




