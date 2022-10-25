from django.core.exceptions import ValidationError
from django import forms

from .validators import email_validator
from .models import User


class UserCreationForm(forms.ModelForm):
    email = forms.EmailField(help_text="Email is required")

    class Meta:
        model = User
        fields = ["email", "password"]

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if not email:
            raise ValidationError("Please provide your email address")
        if not email_validator(email):
            raise ValidationError(
                "please provide a valid Email address")
        return email

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user


class UserLoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(max_length=150, widget=forms.PasswordInput)


# class ResetPasswordForm(forms.Form):
#     password1 = forms.PasswordInput()
#     password2 = forms.PasswordInput()
#
#     def clean_password1(self):
#         password1 = self.cleaned_data.get("password1")
#         password2 = self.cleaned_data.get("password2")
#
#         if not (password1 == password2):
#             raise ValidationError("Passwords don't match")
#         return password1
#
#
# class UserAvatar(forms.Form):
#     avatar = forms.ImageField(required=False)
