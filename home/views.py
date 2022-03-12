from django.shortcuts import render
from exhibition.models import CATEGORY


def home(request):
    """
    Home page view
    """
    category = CATEGORY
    template_name = 'home/index.html'
    context = {
        'category': category
    }
    return render(request, template_name, context)
