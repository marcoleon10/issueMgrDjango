from django.contrib import admin
from .models import Issue

class PostAdmin(admin.ModelAdmin):
    list_display = ["summary", "description", "status", "priority", "reporter", "assignee"]

admin.site.register(Issue, PostAdmin)
