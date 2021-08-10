from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractUser, PermissionsMixin, AbstractBaseUser
from django.urls import reverse
from django.utils import timezone
from django.contrib import messages
from django.template.defaultfilters import slugify
import datetime


# create user
class UserManager(BaseUserManager):
    # create normal user
    def create_user(self, username, email, password=None, is_staff=False, is_active=True, is_admin=False):
        if not username:
            raise ValueError(f'{username} is not available !')
        if not email:
            raise ValueError('Email is required for login !')
        if not password:
            raise ValueError("Password must be 8 characters or longer")
        user = self.model(
            username=username,
            email=email
        )
        user.set_password(password)
        user.staff = is_staff
        user.admin = is_admin
        user.active = is_active
        user.save(using=self._db)
        return user

    # create staff user with lesser privileges
    def create_staff(self, username, email, password=None):
        user = self.create_user(
            username,
            email,
            password=password,
            is_active=True,
            is_staff=True,
            is_admin=False,
        )
        return user

    # create admin user
    def create_superuser(self, username, email, password=None):
        user = self.create_user(
            username,
            email,
            password=password,
            is_active=True,
            is_staff=True,
            is_admin=True,
        )
        return user


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=50, unique=True, blank=False, null=False)
    email = models.EmailField(max_length=100, unique=True, blank=False, null=False)
    active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False)
    admin = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_active(self):
        return self.active

    @property
    def is_staff(self):
        return self.staff

    @property
    def is_admin(self):
        return self.admin

    def get_user_mail(self):
        return self.email

    def __str__(self):
        return self.username

    def get_absolute_url(self):
        return reverse('home', kwargs={'pk': self.pk})


class Profile(models.Model):
    username = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255, default=None, null=True)
    last_name = models.CharField(max_length=255, default=None, null=True)
    email = models.EmailField()
    phone = models.CharField(max_length=13, null=True, blank=True)
    date_of_birth = models.DateTimeField(default=timezone.now)
    biography = models.TextField(null=True)
    website = models.CharField(max_length=150, default=None, null=True)
    avatar = models.ImageField(null=True, upload_to='media/avatar')

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'profile'
        verbose_name_plural = 'profile'

    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'

    def get_short_name(self):
        return f'{self.first_name}'


User.profile = property(lambda user: Profile.objects.get_or_create(username=user)[0])


# post section
class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    slug = models.CharField(max_length=150, unique=True)
    title = models.CharField(
        max_length=300, default=None, null=True, blank=True)
    upload = models.FileField(upload_to='media/posts')
    caption = models.TextField(default=None, null=False, blank=False)
    date_posted = models.DateTimeField(auto_now_add=timezone.now)

    def __str__(self):
        return self.title

    def save(self):
        super(Post, self).save()
        date = datetime.date.today()
        self.slug = '%i/%i/%i/%i-%s' % (
            date.year, date.month, date.day, self.id, slugify(self.title)
        )
        super(Post, self).save()


class Notes(models.Model):
    noted_by = models.OneToOneField(User, on_delete=models.CASCADE)
    notes_on = models.ForeignKey(Post, on_delete=models.CASCADE)
    count = models.IntegerField(default=0)


class Comments(models.Model):
    author = models.ManyToManyField(User)
    comment_on = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment = models.TextField(default=None, null=True, blank=True)
    date_commented = models.DateTimeField(auto_now_add=timezone.now)

    def __str__(self):
        return f'{self.author}: {self.comment_on} '

    class Meta:
        verbose_name = 'Comments'
        verbose_name_plural = "Comments"
