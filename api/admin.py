from django.contrib import admin
from .models import Post, User, Comment


# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ('slug', 'date_posted')
    search_fields = ['author', 'upload']


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'message', 'created_on')
    list_filter = ('author', 'created_on')
    search_fields = ('author', 'created_on')


admin.site.register(Post, PostAdmin)

admin.site.register(User)
