from django.contrib import admin
from .models import Post


@admin.register(Post)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("owner", "created_at", "updated_at", "title", "content", "image", "image_filter")