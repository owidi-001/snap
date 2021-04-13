from django.test import TestCase
from django.urls import reverse
from snapserver.models import Post, User
from django.utils import timezone
from .test_models import UserModelTest


def create_post(self, title='test post1', upload='/home/Desktop/index.jpg',
                caption='test caption'):
    author = UserModelTest().create_normal_user()
    return Post.objects.create(author=author, title=title, caption=caption, upload=upload,
                               date_posted=timezone.now())
