from django.shortcuts import render
# from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from exhibition.models import Post


@login_required
def profile(request):
    """
    User profile page view
    """
    # user = User.objects.get(username=username)
    user = request.user
    posts = Post.objects.filter(user_name=user)
    template_name = 'create/profile.html'
    context = {
        'posts': posts,
        'user': user,
    }
    return render(request, template_name, context)
