from django.contrib import admin
from .models import Post

# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """
    admin panel view of Post model
    """
    list_display = ["title", "content", "author"]