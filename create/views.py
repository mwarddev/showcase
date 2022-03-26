from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from exhibition.models import Post, STATIC_IMAGE
from .forms import NewPostForm


@login_required
def profile(request):
    """
    User profile page view get user posts
    """
    user = request.user
    posts = Post.objects.filter(user_name=user)
    static_images = STATIC_IMAGE
    template_name = 'create/profile.html'
    context = {
        'user': user,
        'posts': posts,
        'static_images': static_images,
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
            messages.success(request, 'You have successfully created a post!')
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
        form = NewPostForm(request.POST, request.FILES, instance=post)

        if form.is_valid():
            edit_post = form.save(commit=False)
            edit_post.post = post
            edit_post.save()
            messages.success(request, 'Your post was successfully edited!')
            return redirect('profile')

    else:
        form = NewPostForm(instance=post)

    context = {
        'backend_form': form,
        'post': post,
    }

    return render(request, template_name, context)


@login_required
def delete_post(request, pk):
    """
    Delete a post
    """
    post_delete = get_object_or_404(Post, pk=pk)
    template_name = 'create/delete_post.html'

    if request.method == 'POST':
        post_delete.delete()
        messages.success(request, 'Your post was successfully deleted')
        return redirect('profile')
    context = {
        'post_delete': post_delete
    }

    return render(request, template_name, context)
