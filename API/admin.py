from django.contrib import admin
from django.contrib.admin import register

from .models import File


# Register your models here.


@register(File)
class FileAdmin(admin.ModelAdmin):
    list_display = ["id", "file_name"]
    list_filter = ["created_at", "updated_at"]

    def file_name(self, obj):
        return obj.file.name.split("/")[-1]

    file_name.short_description = "File Name"
