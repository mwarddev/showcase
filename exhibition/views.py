from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from comments.forms import CommentForm
from .models import Post, STATIC_IMAGE


def get_posts(request, artform):
    """
    Selected artform list view
    """
    static_images = STATIC_IMAGE
    posts = Post.objects.filter(artform__icontains=artform)
    template_name = 'exhibition/posts.html'
    context = {
            'posts': posts,
            'static_images': static_images,
    }
    return render(request, template_name, context)


def get_full_post(request, artform, pk):
    """
    Full post view with comment functionality
    """
    post = get_object_or_404(Post, pk=pk)
    comments = post.comments.all().order_by('created_date')
    static_images = STATIC_IMAGE
    template_name = 'exhibition/full_post.html'

    comment_form = CommentForm(data=request.POST)

    if comment_form.is_valid():
        comment_form.instance.user_name = request.user
        comment = comment_form.save(commit=False)
        comment.post = post
        comment.save()
        messages.success(request, 'Your comment was successfully posted!')
    else:
        comment_form = CommentForm()

    context = {
        'post': post,
        'comments': comments,
        'comment_form': CommentForm(),
        'static_images': static_images,
    }
    return render(request, template_name, context)


def delete_comment(request, artform, pk, comment_id):
    """
    Delete a comment
    """
    post = get_object_or_404(Post, pk=pk)
    comments = post.comments.all()
    comment_to_delete = comments.filter(pk=comment_id)
    template_name = 'comments/delete_comment.html'

    if request.method == 'POST':
        comment_to_delete.delete()
        messages.success(request, 'Your comment was successfully deleted.')
        return redirect('../')

    context = {
        'comment_to_delete': comment_to_delete
    }

    return render(request, template_name, context)
