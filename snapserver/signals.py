from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import User, Profile, Post


# profile signals
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.Profile.save()


# # post signals
# @receiver(post_save, sender=Post)
# def create_post(post_save, instance, created, **kwargs):
#     if created:
#         try:
#             Post.objects.create(user=instance)
#         except:
#             pass
