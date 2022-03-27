from django.db import models
from django.contrib.auth.models import User
from exhibition.models import Post
from comments.models import Comment


class PostLike(models.Model):
    """
    Database model for post likes
    """

    users = models.ForeignKey(User,
                              on_delete=models.CASCADE,
                              related_name='post_likes')
    post = models.ForeignKey(Post,
                             on_delete=models.CASCADE,
                             related_name='post_likes')


class PostDislike(models.Model):
    """
    Database model for post dislikes
    """

    users = models.ForeignKey(User,
                              on_delete=models.CASCADE,
                              related_name='post_dislikes')
    post = models.ForeignKey(Post,
                             on_delete=models.CASCADE,
                             related_name='post_dislikes')


class CommentLike(models.Model):
    """
    Database model for comment likes
    """

    users = models.ForeignKey(User,
                              on_delete=models.CASCADE,
                              related_name='comment_likes')
    comment = models.ForeignKey(Comment,
                                on_delete=models.CASCADE,
                                related_name='comment_likes')


class CommentDislike(models.Model):
    """
    Database model for comment dislikes
    """

    users = models.ForeignKey(User,
                              on_delete=models.CASCADE,
                              related_name='comment_dislikes')
    comment = models.ForeignKey(Comment,
                                on_delete=models.CASCADE,
                                related_name='comment_dislikes')
