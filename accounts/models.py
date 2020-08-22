from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(default='Enter bio')
    image = models.ImageField(default='profile.png', upload_to='profile_pics')
    background=models.ImageField(default='background.jpg', upload_to='profile_pics/walls')


    class Meta:
        verbose_name =("user")
        verbose_name_plural =("users")

    def __str__(self):
        return f'{self.user.username} profile'

    def get_absolute_url(self):
        return reverse("user_detail", kwargs={"pk": self.pk})

    

    # def get_absolute_url(self):
    #     return reverse('post')
