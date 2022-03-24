from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


CATEGORY = (
    ('painting', 'Painting'),
    ('photography', 'Photography'),
    ('sketching', 'Sketching'),
    ('graphic-design', 'Graphic Design'),
    ('fashion', 'Fashion'),
    ('sculpture', 'Sculpture'),
    ('architecture', 'Architecture'),
    ('fine-art', 'Fine Art')
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
