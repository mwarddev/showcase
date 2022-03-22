from django.shortcuts import render, get_object_or_404
from comments.forms import CommentForm
from .models import Post, CATEGORY


def get_posts(request, artform):
    """
    Selected artform list view
    """
    category = CATEGORY
    posts = Post.objects.filter(artform__icontains=artform)
    template_name = 'exhibition/posts.html'
    context = {
            'posts': posts,
            'category': category,
    }
    return render(request, template_name, context)


def get_full_post(request, artform, pk):
    """
    Full post view
    """
    queryset = Post.objects.all()
    post = get_object_or_404(queryset, pk=pk)
    comments = post.comments.all().order_by('created_date')
    category = CATEGORY
    template_name = 'exhibition/full_post.html'

    comment_form = CommentForm(data=request.POST)

    if comment_form.is_valid():
        comment_form.instance.user_name = request.user
        comment = comment_form.save(commit=False)
        comment.post = post
        comment.save()
    else:
        comment_form = CommentForm()

    context = {
        'post': post,
        'comments': comments,
        'comment_form': CommentForm(),
        'category': category,
    }
    return render(request, template_name, context)
