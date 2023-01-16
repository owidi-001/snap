import random
from threading import Thread

from django.contrib.auth import authenticate
from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import get_object_or_404
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView

# forms
from .forms import UserCreationForm, UserLoginForm, UserAvatar
# models
from .models import User
# serializers
from .send_email import send_mail
from .serializers import UserSerializer, PasswordSerializer, RegisterSerializer
from .token_generator import password_reset_token
from .schema import RegistrationSchema, LoginSchema, ResetPasswordSchema


class EmailThead(Thread):
    def __init__(self, email_to, message, subject):
        super().__init__()
        self.email_to = email_to
        self.message = message
        self.subject = subject

    def run(self):
        send_mail(self.message, self.email_to, self.subject)


class UserView(APIView):
    """
    Retrieve, update or delete a user instance.
    """

    def get(self, request, pk, format=None):
        user = get_object_or_404(User, id=pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        user = get_object_or_404(User, id=pk)
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        user = get_object_or_404(User, id=pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class RegisterView(APIView):
    """
        The user fills the required parameters namely (email,password).
        The form is checked for validity and user saved if valid otherwise relevant exception is thrown.
        """

    schema = RegistrationSchema()

    def post(self, request):
        form = UserCreationForm(request.data)

        if form.is_valid():
            user = form.save()
            data = RegisterSerializer(user).data
            # create auth token
            token = Token.objects.get(user=user).key
            data['token'] = token

            email_to = form.cleaned_data.get("email")
            message = render_to_string("account/registration_email.html", {
                "email": email_to})
            subject = "Registration confirmation"
            send_mail(message, [email_to], subject)

            EmailThead([email_to], message, subject).start()
            data[f'message':"Account creation for {email_to}"]

            return Response(data, status=200)

        return Response(form.errors, status=400)


class LoginView(APIView):
    """
    User logs in with the required credentials
    """
    schema = LoginSchema()

    def post(self, request):
        form = UserLoginForm(request.data)
        if form.is_valid():
            user = authenticate(email=form.cleaned_data["email"],
                                password=form.cleaned_data["password"])
            if user:
                token = Token.objects.get(user=user).key
                # token=Token.objects.get_or_create(user=user).key
                print(token)
                data = UserSerializer(user).data
                data["token"] = token

                return Response(data, status=200)
            return Response({"errors": ["please provide valid credentials"]},
                            status=400)
        return Response(form.errors, status=400)


class ResetPasswordView(APIView):
    """
    User gets to reset a forgotten password using their registration email
    """

    schema = ResetPasswordSchema()

    def post(self, request):
        """
        Request pass word reset by providing an email.

        short code to be used to change password
        short code will be sent to the user which will be used to reset the password
        instead of sending long password reset token generated by django PasswordResetGenerator
        """
        serializer = PasswordSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.data.get("email")
            user = User.objects.filter(
                email=email).first()
            if not user:
                return Response({"email": ["User not found"]}, status=400)
            site = get_current_site(request)
            token = password_reset_token.make_token(user)
            uid64 = urlsafe_base64_encode(force_bytes(user.pk))

            scheme = request.build_absolute_uri().split(":")[0]
            path = f"{scheme}://{request.get_host()}/auth/reset/{uid64}/{token}"
            subject = "Password Reset"
            print(path)
            message = render_to_string('account/password_reset_mail.html', {
                'user': user,
                "path": path
            })

            EmailThead([email], message, subject).start()

            return Response(
                {"message": f"please check code sent to {email} to change your password",
                 },
                status=200)
        return Response(serializer.errors, status=400)

    @staticmethod
    def gen_token():
        token = ""
        for _ in range(6):
            token += "1234567890"[random.randint(0, 9)]
        return int(token)


class UserAddAvatar(APIView):
    def patch(self, request):
        """update user avatar"""
        form = UserAvatar(request.FILES)

        if form.is_valid():
            if request.FILES:
                user = User.objects.get(user=request.user)
                user.avatar = request.FILES[0]
                user.save()
                return Response(
                    {"message": "avatar updated successfully"}, status=status.HTTP_200_OK
                )
            return Response(
                {"message": "invalid image"}, status=status.HTTP_400_BAD_REQUEST
            )
