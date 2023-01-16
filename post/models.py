from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.utils.text import slugify
from django.conf import settings

def post_upload(instance, filename):
    return f"posts/{instance.author.id}/{filename}"



# Create your models here.
class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='posts', on_delete=models.CASCADE)
    upload = models.ImageField(upload_to=post_upload, blank=False, null=False, unique=True)
    slug = models.SlugField(max_length=255, default=None, blank=True, null=True)
    caption = models.TextField(default=None, null=True, blank=True, help_text='What is the story behind this?')
    date_posted = models.DateTimeField(auto_now_add=timezone.now)

    def __str__(self):
        return self.slug

    def save(self, *args, **kwargs):
        self.slug = self.slug or slugify(self.upload)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})