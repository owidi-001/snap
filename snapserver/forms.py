from django import forms
from .models import User,Profile,Post,Comment
from django.contrib.auth.forms import UserCreationForm


# user forms

class UserRegisterForm(UserCreationForm):
    email=forms.EmailField()

    class Meta:
        model=User
        fields=['email','password1','password2']

        # validate data received


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields='__all__'

    def clean_avatar(self):
        avatar = self.cleaned_data['avatar']

        try:
            w, h = get_image_dimensions(avatar)

            #validate dimensions
            max_width = max_height = 100
            if w > max_width or h > max_height:
                raise forms.ValidationError(
                    u'Please use an image that is '
                     '%s x %s pixels or smaller.' % (max_width, max_height))

            #validate content type
            main, sub = avatar.content_type.split('/')
            if not (main == 'image' and sub in ['jpeg', 'pjpeg', 'gif', 'png']):
                raise forms.ValidationError(u'Please use a JPEG, '
                    'GIF or PNG image.')

        except AttributeError:
            """
            Handles case when we are updating the user profile
            and do not supply a new avatar
            """
            # set default avatar
            pass

        return avatar


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
        model = Comment
        fields = [
            'body'
        ]
