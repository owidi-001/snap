from django.contrib import admin
from .models import Post, User #, Comment


# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'date_posted')
    # list_filter = ("status",)
    search_fields = ['title', 'caption']
    prepopulated_fields = {'slug': ('title',)}


# @admin.register(Comment)
# class CommentAdmin(admin.ModelAdmin):
#     list_display = ('name', 'body', 'post', 'created_on', 'active')
#     list_filter = ('active', 'created_on')
#     search_fields = ('name', 'email', 'body')
#     actions = ['approve_comments']
#
#     def approve_comments(self, request, queryset):
#         queryset.update(active=True)


admin.site.register(Post, PostAdmin)

admin.site.register(User)
