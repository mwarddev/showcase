from django.shortcuts import render
from exhibition.models import STATIC_IMAGE


def home(request):
    """
    Home page view
    """
    static_images = STATIC_IMAGE
    template_name = 'home/index.html'
    context = {
        'static_images': static_images
    }
    return render(request, template_name, context)
