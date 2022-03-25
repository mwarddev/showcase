from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


CATEGORY = (
    ('Painting', 'painting'),
    ('Photography', 'photography'),
    ('Sketching', 'sketching'),
    ('Graphic Design', 'graphic-design'),
    ('Fashion', 'fashion'),
    ('Sculpture', 'sculpture'),
    ('Architecture', 'architecture'),
    ('Fine Art', 'fine-art')
)

STATIC_IMAGE = (
    ('Painting', 'images/painting.jpg'),
    ('Photography', 'images/photography.jpg'),
    ('Sketching', 'images/sketching.jpg'),
    ('Graphic Design', 'images/graphic-design.jpg'),
    ('Fashion', 'images/fashion.jpg'),
    ('Sculpture', 'images/sculpture.jpg'),
    ('Architecture', 'images/architecture.jpg'),
    ('Fine Art', 'images/fine-art.jpg')
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
    title = models.CharField(max_length=200, null=False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    description = models.TextField(null=False)
    image = CloudinaryField('image',
                            transformation={
                                'aspect_ratio': '4:3',
                                'crop': 'fill',
                                'gravity': 'auto'
                            },
                            default='placeholder')

    class Meta:
        """
        Helper methods for the Post model
        """
        ordering = ['-created_date']

    def __str__(self):
        return f"{self.title}"
