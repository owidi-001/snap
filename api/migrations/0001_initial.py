# Generated by Django 3.2.7 on 2022-01-08 19:40

import api.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('email', models.EmailField(help_text='email address', max_length=254, unique=True)),
                ('first_name', models.CharField(blank=True, help_text='first name', max_length=30)),
                ('last_name', models.CharField(blank=True, help_text='last name', max_length=30)),
                ('date_joined', models.DateTimeField(auto_now_add=True, help_text='date joined')),
                ('is_active', models.BooleanField(default=True, help_text='active')),
                ('avatar', models.ImageField(blank=True, default='avatar.png', null=True, upload_to='avatars')),
                ('phone', models.CharField(blank=True, max_length=13, null=True)),
                ('biography', models.TextField(null=True)),
                ('website', models.URLField(default=None, max_length=150, null=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
            },
            managers=[
                ('objects', api.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('upload', models.FileField(upload_to='posts')),
                ('title', models.CharField(default=None, help_text='Give your post a context', max_length=300)),
                ('slug', models.SlugField(blank=True, default=None, max_length=255, null=True)),
                ('caption', models.TextField(blank=True, default=None, help_text='Add a little story to this', null=True)),
                ('date_posted', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='api.post')),
            ],
            options={
                'ordering': ['created_on'],
            },
        ),
    ]
