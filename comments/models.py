from django.db import models
from django.contrib.auth.models import User
from exhibition import Post


class Comments(models.Model):
    """
    Database model for user comments
    """

    post = models.ForeignKey(Post, on_delete=models.CASCADE,
                             related_name='comments')
    user_name = models.ForeignKey(User, on_delete=models.CASCADE,
                                  related_name='user_comment')
    body = models.TextField(blank=False)
    created_date = models.DateTimeField(auto_now=True)
    comment_like = models.ManyToManyField(User,
                                          related_name='comment_likes',
                                          blank=True)
    comment_dislike = models.ManyToManyField(User,
                                             related_name='comment_dislikes',
                                             blank=True)
    comment_report = models.ManyToManyField(User,
                                            related_name='comment_report',
                                            blank=True)

    class Meta:
        """
        Helper methods for the Comments model
        """
        ordering = ['created_date']

    def __str__(self):
        return f"Comment {self.user_name} {self.body}"

    def likes_count(self):
        return self.comment_like.count()

    def dislikes_count(self):
        return self.comment_dislike.count()
