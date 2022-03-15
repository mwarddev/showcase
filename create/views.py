from django.shortcuts import render
from django.contrib.auth.models import User
from exhibition.models import Post


def profile(request, username):
    """
    User profile page view
    """
    user = User.objects.get(username=username)
    post = Post.objects.filter(user_name=user)
    template_name = 'create/profile.html'
    context = {
        'post': post,
        'user': user,
    }
    return render(request, template_name, context)
