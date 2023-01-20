from django.contrib import admin

from .models import Follow

# Register your models here.
class FollowAdmin(admin.ModelAdmin):
    list_display=[
        "followed","follower"
    ]
    list_filter=["followed","follower"]

admin.site.register(Follow,FollowAdmin)