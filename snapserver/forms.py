from django import forms
from .models import User, Profile, Post, Comments
from django.contrib.auth.forms import UserCreationForm


# user forms
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['avatar']


# post forms
class CreatePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            "title",
            "caption",
            'upload'
        ]


class CreateCommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = [
            'comment'
        ]
