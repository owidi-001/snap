from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

# forms
from snapserver.forms import UserCreationForm

# models
from .models import User

# serializers
from .serializers import UserSerializer


class UserListView(APIView):

    # retrieve user data
    def get(self, request, format=None):
        """
        Return a list of all users.
        """
        usernames = [user.email for user in User.objects.all()]
        return Response(usernames)

    # create new user
    def post(self, request):
        form = UserCreationForm(request.data)
        if form.is_valid():
            username = form.cleaned_data["email"]
            user = form.save()
            data = UserSerializer(user).data
            form.message(f'{username} registered successfully')
            return Response(data, status=200)
        else:
            form.add_error("Form invalid")
            form = UserCreationForm()
        return Response(form.errors, status=400)


class UserDetail(APIView):
    """
    Retrieve, update or delete a user instance.
    """

    def get_object(self, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        user = self.get_object(pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        user = self.get_object(pk)
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        user = self.get_object(pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
