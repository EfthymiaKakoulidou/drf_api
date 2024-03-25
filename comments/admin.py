from django.contrib import admin
from .models import Comment


@admin.register(Comment)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("owner", "post", "created_at", "updated_at", "content")