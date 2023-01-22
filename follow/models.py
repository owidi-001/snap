from django.db import models
from user.models import User

# Create your models here.
class Follow(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name="follows")
    follower=models.ForeignKey(User,on_delete=models.CASCADE,related_name="following")