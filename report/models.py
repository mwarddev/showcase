from django.db import models
from django.contrib.auth.models import User
from exhibition.models import Post
from comments.models import Comment


class PostReport(models.Model):
    """
    Database model for reporting a post
    """

    reporting_user = models.ForeignKey(User,
                                       on_delete=models.CASCADE,
                                       related_name='report_post')
    reported_post = models.ForeignKey(Post,
                                      on_delete=models.CASCADE,
                                      related_name='report_post')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


class CommentReport(models.Model):
    """
    Database model for reporting a comment
    """

    reporting_user = models.ForeignKey(User,
                                       on_delete=models.CASCADE,
                                       related_name='report_comment')
    reported_comment = models.ForeignKey(Comment,
                                         on_delete=models.CASCADE,
                                         related_name='report_comment')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
