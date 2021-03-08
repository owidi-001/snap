from django import forms
from .models import Post,Comment


class CreatePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            "upload",
            "content",
        ]

class CreateCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = [
            'body'
        ]