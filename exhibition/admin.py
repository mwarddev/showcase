from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Post


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    """
    Configure admin page for posts
    """

    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('artform', 'created_date')
    list_display = ('title', 'slug', 'artform', 'created_date')
    search_fields = ['user_name', 'title', 'description']
    summernote_fields = ('description')
