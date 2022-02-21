from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

STATUS = ((0, 'Draft'), (1, 'Published'))
CATEGORY = ((0, 'Painting'),
            (1, 'Photography'),
            (2, 'Music'),
            (3, 'Graphic Design'),
            (4, 'Fashion'),
            (5, 'Sculpture'),
            (6, 'Architecture'),
            (7, 'Fine Art'))


class Post(models.Model):
    """
    Database model for user posts
    """

    user_name = models.ForeignKey(User, on_delete=models.CASCADE,
                                  related_name='posts')
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    art_form = models.IntegerField(choices=CATEGORY, default=0)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    description = models.TextField()
    media = CloudinaryField('Media', default='placeholder')
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        """
        Helper methods for the Post model
        """
        ordering = ['-created_date']

    def __str__(self):
        return f"{self.title}"
