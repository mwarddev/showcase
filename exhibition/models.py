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
    ('Painting',
    'https://res.cloudinary.com/mwarddev/image/upload/v1647725825/static/images/painting.jpg'),
    ('Photography',
    'https://res.cloudinary.com/mwarddev/image/upload/v1647725826/static/images/photography.jpg'),
    ('Sketching',
    'https://res.cloudinary.com/mwarddev/image/upload/v1647725826/static/images/sketching.jpg'),
    ('Graphic Design',
    'https://res.cloudinary.com/mwarddev/image/upload/v1647725827/static/images/graphic-design.jpg'),
    ('Fashion',
    'https://res.cloudinary.com/mwarddev/image/upload/v1647725828/static/images/fashion.jpg'),
    ('Sculpture',
    'https://res.cloudinary.com/mwarddev/image/upload/v1647725829/static/images/sculpture.jpg'),
    ('Architecture',
    'https://res.cloudinary.com/mwarddev/image/upload/v1647725828/static/images/architecture.jpg'),
    ('Fine Art',
    'https://res.cloudinary.com/mwarddev/image/upload/v1647725827/static/images/fine-art.jpg')
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
