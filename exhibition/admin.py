from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Post


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    """
    Configure admin page for posts
    """

    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('art_form', 'created_date')
    list_display = ('title', 'slug', 'art_form', 'created_date')
    search_fields = ['user_name', 'title', 'description']
    summernote_fields = ('description')
