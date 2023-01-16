from django.contrib import admin
from .models import Resource

class ResourceAdmin(admin.ModelAdmin):
    list_display = ("title", "language",)

admin.site.register(Resource, ResourceAdmin)