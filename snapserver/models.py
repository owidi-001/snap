from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractUser, PermissionsMixin
from django.utils import timezone


# create user
class UserManager(BaseUserManager):
    # create normal user
    def create_user(self, email, password=None, is_active=True, is_admin=False):
        if not email:
            raise ValueError('Email is required for login !')
        user = self.model(
            email=self.email
        )
        user.set_password(password)
        user.admin = is_admin
        user.active = is_active
        user.save(using=self._db)
        return user

    # create admin user
    def create_superuser(self, email, password=None):
        user = self.create_user(
            email,
            password=password,
            is_active=True,
            is_admin=True,
        )
        return user


class User(AbstactBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=100, unique=True)
    active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False)
    admin = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        return True

    @property
    def is_active(self):
        return self.active

    @property
    def is_admin(self):
        return self.admin


class Profile(models.Model):
    first_name = models.CharField(max_length=255, default=None)
    last_name = models.CharField(max_length=255, default=None)
    email = models.OneToOneField(User, on_delete=models.CASCADE)
    biography = models.TextField()
    avatar = models.ImageField(null=True, upload_to='media/avatar')

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        return True

    class Meta:
        verbose_name = 'profile'
        verbose_name_plural = 'profile'

    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'

    def get_short_name(self):
        return f'{self.first_name}'


# post section
class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(
        max_length=300, default=None, null=True, blank=True)
    upload = models.FileField(upload_to='media/posts')
    caption = models.TextField(default=None, null=True, blank=True)
    date_posted = models.DateTimeField(auto_now_add=timezone.now)
    notes = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.title} posted by {self.author}'


class Comments(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField(default=None, null=True, blank=True)
    date_commented = models.DateTimeField(auto_now_add=timezone.now)

    def __str__(self):
        return f'{self.author}'

    class Meta:
        verbose_name = 'Comments'
        verbose_name_plural = "Comments"
