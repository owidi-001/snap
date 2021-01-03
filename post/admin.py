'''
CUSTOMIZE THE ADMIN SITE AND RESTRICT VIEWS AND ACCESS ONLY BY THE ADMIN [OWIDI]
'''
from django.contrib import admin
from .models import Post, Comment,Likes


# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ('user','upload','date_posted')


admin.site.register(Post, PostAdmin)
admin.site.register(Comment)
admin.site.register(Likes)
