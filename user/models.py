import datetime
from _datetime import datetime

from django.conf import settings
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.core.mail import send_mail
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

from .managers import UserManager


def avatar_upload(instance, filename):
    return f"avatars/{instance.user.id}/{datetime.now()}/{filename}"


# User
class User(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(help_text='first name', max_length=30, blank=True)
    last_name = models.CharField(help_text='last name', max_length=30, blank=True)
    email = models.EmailField(help_text='email address', unique=True)
    date_joined = models.DateTimeField(help_text='date joined', auto_now_add=True)
    is_active = models.BooleanField(help_text='active', default=False)
    avatar = models.ImageField(upload_to=avatar_upload, default="avatars/avatar.png")
    bio = models.CharField(max_length=200, blank=True, null=True)
    website = models.URLField(max_length=200, default=None, null=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'

    def get_full_name(self):
        """
        Returns the first_name plus the last_name, with a space in between.
        """
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        """
        Returns the short name for the user.
        """
        return self.first_name

    def email_user(self, subject, message, from_email=settings.EMAIL_HOST_USER, **kwargs):
        """
        Sends an email to this User.
        """
        send_mail(subject, message, from_email, [self.email], **kwargs)

    @property
    def is_staff(self):
        """Is the user a member of staff?"""
        # Simplest possible answer: All admins are staff
        return self.is_superuser

    def __str__(self):
        return self.email


@receiver(post_save, sender=User)
def create_auth_token(sender=None, instance=None, created=False, **kwargs):
    """
     generate authentication  token after a user has been created and send him/her an email
    """
    if created:
        Token.objects.create(user=instance)