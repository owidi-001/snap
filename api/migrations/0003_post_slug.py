# Generated by Django 3.2.7 on 2021-09-19 05:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.SlugField(blank=True, default=None, max_length=255, null=True),
        ),
    ]
