from django.shortcuts import render
from .models import Post


def get_posts(request, artform):
    """
    Selected artform list view
    """
    posts = Post.objects.filter(artform__icontains=artform)
    template_name = 'exhibition/posts.html'
    context = {
            'posts': posts
    }
    return render(request, template_name, context)


def get_full_post(request, artform, pk):
    """
    Full post view
    """
    post = Post.objects.filter(pk=pk)
    template_name = 'exhibition/full_post.html'
    context = {
        'post': post
    }
    return render(request, template_name, context)


# class CategorySelect(generic.ListView):
#     """
#     View for artform choice on home page
#     """
#     model = Post
#     template_name = 'index.html'

#     def get(self, request, *args, **kwargs):
#         context = {
#             'category': CATEGORY
#         }
#         return render(request, 'index.html', context)


# class SelectedCategory(generic.ListView):
#     """
#     View for selected artform list
#     """
#     model = Post
#     template_name = 'exhibition/posts.html'

#     def get_queryset(self, *args, **kwargs):
#         return Post.objects.filter(artform__icontains=self.kwargs.get('artform'))




# class FullPostView(generic.DetailView):
#     """
#     View for viewing full post
#     """

#     model = Post
#     template_name = 'exhibition/full_post.html'
