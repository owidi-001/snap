'''
TO DO:
LIMIT THE NUMBER OF TEXT CHARACTERS SOMEONE CAN COMMENT FOR PROPER VIEWS AND PAGINATION
'''

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
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    post=models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    body=models.TextField(default='No comments',blank=True)
    date_added=models.DateTimeField(auto_now=timezone.now)

    def __str__(self):
        return f'{self.body} by {self.user}'

class Likes(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    post=models.ForeignKey(Post, on_delete=models.CASCADE)
    count= models.IntegerField(default=0)
    
    def __str__(self):
        return self.count

    class Meta:
        db_table = 'Likes'
        managed = True
        verbose_name = 'Like'
        verbose_name_plural = 'Likes'
