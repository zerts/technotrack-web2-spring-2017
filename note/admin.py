from django.contrib import admin

from .models import Post, Comment, Like
from django.contrib.contenttypes.admin import GenericInlineModelAdmin

# Register your models here.

class CommentInline(admin.TabularInline):
    model = Comment
    extra = 1


class LikeInline(admin.TabularInline, GenericInlineModelAdmin):
    model = Like
    fk_name = 'likes'
    ct_field = 'target_content_type'
    ct_fk_field = 'target_id'
    extra = 1


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    inlines = CommentInline, LikeInline,


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    inlines = LikeInline,


@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    pass


# Register your models here.
