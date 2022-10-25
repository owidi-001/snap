from datetime import datetime

from django.conf import settings
from django.db import models
from django.urls import reverse
from django.utils.text import slugify


def post_upload(instance, filename):
    return f"posts/{instance.author.id}/{datetime.now()}/{filename}"


# Post model
class Blog(models.Model):
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='blogs', on_delete=models.CASCADE)
    upload = models.FileField(upload_to=post_upload, blank=True, null=True)
    slug = models.SlugField(max_length=255, default=None, blank=True, null=True)
    caption = models.TextField(default=None, null=True, blank=True, help_text='Give us a story')
    date_posted = models.DateTimeField(auto_now_add=datetime.now)

    def __str__(self):
        return self.slug

    def save(self, *args, **kwargs):
        self.slug = self.slug or slugify(self.upload)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})
