from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.utils import timezone

class Post(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    upload = models.ImageField(blank=True, null=True,upload_to ='media/media') 
    caption=models.TextField()
    date_posted=models.DateField(auto_now=timezone.now)

    def __str__(self):
        return self.date_posted

    def get_absolute_url(self):
        return reverse("post", kwargs={"pk": self.pk})


class Comment(models.Model):
    post=models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    name=models.CharField(max_length=200)
    body=models.TextField(blank=True)
    date_added=models.DateTimeField(auto_now=timezone.now)

    def __str__(self):
        return f'%s %s' (self.post.date_posted, self.name)