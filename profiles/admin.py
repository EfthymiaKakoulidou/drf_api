from django.contrib import admin
from .models import Profile


@admin.register(Profile)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("owner", "created_at", "updated_at", "name", "content", "image")