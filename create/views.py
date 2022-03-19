from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from exhibition.models import Post
from .forms import NewPostForm


@login_required
def profile(request):
    """
    User profile page view get user posts
    """
    user = request.user
    posts = Post.objects.filter(user_name=user)
    template_name = 'create/profile.html'
    context = {
        'user': user,
        'posts': posts,
    }
    return render(request, template_name, context)


@login_required
def create_post(request):
    """
    Create a new post
    """
    context = dict(backend_form=NewPostForm())

    if request.method == 'POST':
        form = NewPostForm(request.POST, request.FILES)
        form.instance.user_name = request.user

        context['posted'] = form.instance
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.post = Post
            new_post.save()

            return redirect('profile')
        else:
            form = NewPostForm()

    return render(request, 'create/new_post.html', context)
