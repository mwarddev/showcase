from django.contrib import admin
from .models import PostReport, CommentReport


@admin.register(PostReport)
class PostReportAdmin(admin.ModelAdmin):
    """
    Configure admin page for post reports
    """
    list_display = ('reported_post',
                    'reporting_user',
                    'created',
                    'reason',
                    'more_info')
    list_filter = ('created', 'reported_post', 'reporting_user', 'reason')
    search_fields = ['reported_post', 'reporting_user', 'reason', 'more_info']


@admin.register(CommentReport)
class CommentReportAdmin(admin.ModelAdmin):
    """
    Configure admin page for comment reports
    """
    list_display = ('reported_comment',
                    'reporting_user',
                    'created', 'reason',
                    'more_info')
    list_filter = ('created', 'reported_comment', 'reporting_user', 'reason')
    search_fields = ['reported_comment',
                     'reporting_user',
                     'reason',
                     'more_info']
