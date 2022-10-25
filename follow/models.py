from django.conf import settings
from django.db import models


# Create your models here.

# # followers
class Follow(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    follow = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="follow", on_delete=models.CASCADE)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['user', 'follow'], name='user follow')
        ]
        verbose_name_plural = "Following"

    def __str__(self):
        return f"""{self.user} follows {self.follow}"""
