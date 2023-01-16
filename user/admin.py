from django.contrib import admin
from .models import User

# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display=['email', 'first_name', 'last_name', 'phone', 'website', 'biography', 'avatar']
    list_filter=['email', 'phone', 'website',]

admin.site.register(UserAdmin,User)