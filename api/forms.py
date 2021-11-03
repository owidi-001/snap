from django import forms
from django.core.exceptions import ValidationError

from .models import User, Post #, Comment
from django.contrib.auth.forms import UserCreationForm


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['upload', 'title', 'caption']


class PostUpdateForm(forms.Form):
    class Meta:
        model = Post
        fields = ['upload', 'title', 'caption']


# class PostCommentForm(forms.ModelForm):
#     class Meta:
#         model = Comment
#         fields = ['body']


# user forms
class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(label='Email')
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ["email", "password1", "password2"]

    def email_clean(self):
        email = self.cleaned_data['email'].lower()
        new = User.objects.filter(email=email)
        if new.count():
            raise ValidationError(" Email Already Exist")
        return email

    def clean_password2(self):
        password1 = self.cleaned_data['password1']
        password2 = self.cleaned_data['password2']

        if password1 and password2 and password1 != password2:
            raise ValidationError("Password don't match")
        return password2

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user
