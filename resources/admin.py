from django.contrib import admin
from .models import Resource, Comment


class CommentInline(admin.TabularInline):
    model = Comment


class ResourceAdmin(admin.ModelAdmin):
    inlines = [
        CommentInline,
    ]
    list_display = ("title", "language",)

admin.site.register(Resource, ResourceAdmin)