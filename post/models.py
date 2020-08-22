from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.utils import timezone

class Post(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    title=models.CharField(max_length=150,blank=True,null=True)
    subtitle=models.CharField(max_length=300,blank=True,null=True)
    upload = models.ImageField(blank=True, null=True,upload_to ='media/') 
    caption=models.TextField()
    date_posted=models.DateField(auto_now=timezone.now)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("post", kwargs={"pk": self.pk})


