from django.contrib import admin
from .models import Comment


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """
    Configure admin page for comments
    """

    list_display = ('user_name', 'post', 'body', 'created_date')
    list_filter = ('created_date', 'user_name')
    search_fields = ['user_name', 'body']
