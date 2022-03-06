from django.shortcuts import render, get_object_or_404, reverse
from django.http import HttpResponseRedirect
from django.views import generic, View
from .models import Post, CATEGORY


class CategorySelect(generic.ListView):
    """
    View for artform choice on home page
    """
    model = Post
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        context = {
            'category': CATEGORY
        }
        return render(request, 'index.html', context)


class SelectedCategory(generic.ListView):
    """
    View for selected artform list
    """
    model = Post
    template_name = 'posts.html'

    def get_queryset(self, *args, **kwargs):
        return Post.objects.filter(artform__icontains=self.kwargs.get('artform'))


class FullPostView(generic.DetailView):
    """
    View for viewing full post
    """

    model = Post
    template_name = 'full_post.html'
