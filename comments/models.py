from django.db import models
from django.contrib.auth.models import User
from exhibition.models import Post


class Comment(models.Model):
    """
    Database model for user comments
    """

    post = models.ForeignKey(Post, on_delete=models.CASCADE,
                             related_name='comments')
    user_name = models.ForeignKey(User, on_delete=models.CASCADE,
                                  related_name='user_comment')
    body = models.TextField(blank=False)
    created_date = models.DateTimeField(auto_now=True)
    report_comment = models.ForeignKey(User,
                                       on_delete=models.CASCADE,
                                       related_name='report_comment', default=False)

    class Meta:
        """
        Helper methods for the Comments model
        """
        ordering = ['created_date']

    def __str__(self):
        return f"Comment {self.user_name} {self.body}"
