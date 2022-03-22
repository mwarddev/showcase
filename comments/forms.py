from .models import Comment
from django import forms


class CommentForm(forms.ModelForm):
    """
    Form class for adding comments
    """
    class Meta:
        """
        Target model and form field/s to display
        """
        model = Comment
        fields = ['body']
        labels = {
            'body': 'Comment below'
        }
