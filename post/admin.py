from django.contrib import admin

# Register your models here.
from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display=[
        "author","date_posted","slug"
    ]
    list_filter=[
        "author","date_posted",
    ]


admin.site.register(PostAdmin,Post)