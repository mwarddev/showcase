from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

STATUS = (
    (0, 'Draft'),
    (1, 'Published')
)

CATEGORY = (
    ('Painting', 'Painting'),
    ('Photography', 'Photography'),
    ('Music', 'Music'),
    ('Graphic Design', 'Graphic Design'),
    ('Fashion', 'Fashion'),
    ('Sculpture', 'Sculpture'),
    ('Architecture', 'Architecture'),
    ('Fine Art', 'Fine Art')
)


class Post(models.Model):
    """
    Database model for user posts
    """

    user_name = models.ForeignKey(User, on_delete=models.CASCADE,
                                  related_name='posts')
    artform = models.CharField(max_length=20,
                               choices=CATEGORY,
                               default='Painting')
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
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
