from django.urls import reverse
from django.utils import timezone
from django.db import models
from django.core.mail import send_mail
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.utils.text import slugify
from django.contrib.auth.base_user import BaseUserManager
from django.conf import settings


def avatar_upload(instance, filename):
    return f"avatars/{instance.user.id}/{filename}"


def post_upload(instance, filename):
    return f"posts/{instance.author.id}/{filename}"


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(help_text='email address', unique=True)
    first_name = models.CharField(help_text='first name', max_length=30, blank=True)
    last_name = models.CharField(help_text='last name', max_length=30, blank=True)
    date_joined = models.DateTimeField(help_text='date joined', auto_now_add=True)
    is_active = models.BooleanField(help_text='active', default=True)
    avatar = models.ImageField(upload_to=avatar_upload, default="avatars/avatar.png", null=True, blank=True)
    phone = models.CharField(max_length=13, null=True, blank=True)
    biography = models.TextField(null=True)
    website = models.URLField(max_length=150, default=None, null=True)

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

    def email_user(self, subject, message, from_email=None, **kwargs):
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
        return self.email.split("@")[0]


# post section
class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='posts', on_delete=models.CASCADE)
    upload = models.ImageField(upload_to=post_upload, blank=False, null=False,unique=True)
    slug = models.SlugField(max_length=255, default=None, blank=True, null=True)
    caption = models.TextField(default=None, null=True, blank=True, help_text='Add a little story to this')
    date_posted = models.DateTimeField(auto_now_add=timezone.now)

    def __str__(self):
        return self.slug

    def save(self, *args, **kwargs):
        self.slug = self.slug or slugify(self.upload)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    message = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return 'Comment {} by {}'.format(self.message, self.author)
