from django import forms
from exhibition.models import Post


class NewPostForm(forms.ModelForm):
    """
    New post form class
    """
    class Meta:
        """
        New post form meta
        """
        model = Post
        fields = [
            'artform',
            'title',
            'description',
            'image',
        ]
