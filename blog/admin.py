from django.contrib import admin
from .models import Post,Comment


# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'publish', 'status']
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'publish'

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = []