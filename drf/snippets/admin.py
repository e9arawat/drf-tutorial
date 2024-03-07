from django.contrib import admin

from .models import Snippet

# Register your models here.


@admin.register(Snippet)
class SnippetAdmin(admin.ModelAdmin):
    """
    Snippet model on admin panel
    """

    list_display = ["id", "title", "code", "linenos", "language", "style"]
