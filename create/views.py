from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from exhibition.models import Post, CATEGORY
from .forms import NewPostForm


@login_required
def profile(request):
    """
    User profile page view get user posts
    """
    user = request.user
    posts = Post.objects.filter(user_name=user)
    category = CATEGORY
    template_name = 'create/profile.html'
    context = {
        'user': user,
        'posts': posts,
        'category': category,
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


@login_required
def update_post(request, pk):
    """
    Edit a post
    """
    template_name = 'create/edit_post.html'
    post = get_object_or_404(Post, pk=pk)

    if request.method == 'POST':
        form = NewPostForm(request.POST, instance=post)

        if form.is_valid():
            form.save()

    else:
        form = NewPostForm(instance=post)

    context = {
        'backend_form': form,
        'post': post,
    }

    return render(request, template_name, context)
