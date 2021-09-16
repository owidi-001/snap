from django import forms
from .models import User, Post,Comment
from django.contrib.auth.forms import UserCreationForm


class PostCreateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['upload', 'title', 'caption']


class PostUpdateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['upload', 'title', 'caption']


class PostCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment']


# user forms
class UserCreationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["email", "password"]

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user
