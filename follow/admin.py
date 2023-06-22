from django.contrib import admin

from .models import Follow

# Register your models here.
class FollowAdmin(admin.ModelAdmin):
    list_display=[
        "user","follower"
    ]
    list_filter=["user","follower"]

admin.site.register(Follow,FollowAdmin)