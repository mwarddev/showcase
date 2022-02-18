from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

STATUS = ((0, 'Draft'), (1, 'Published'))


class Post(models.Model):
    """
    Database model for user posts
    """

    user_name = models.ForeignKey(User, on_delete=models.CASCADE,
                                  related_name='posts')
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    created_date = models.DateTimeField(auto_now=True)
    updated_date = models.DateTimeField(auto_now=True)
    description = models.TextField()
    media = CloudinaryField('image', resource_type='video',
                            default='placeholder')
    status = models.IntegerField(choices=STATUS, default=0)
    like = models.ManyToManyField(User, related_name='likes', blank=True)
    dislike = models.ManyToManyField(User, related_name='dislikes', blank=True)
    report = models.ManyToManyField(User, related_name='report', blank=True)

    class Meta:
        """
        Helper methods for the Post model
        """
        ordering = ['-created_date']

    def __str__(self):
        return self.title

    def likes_count(self):
        return self.like.count()

    def dislikes_count(self):
        return self.dislike.count()
