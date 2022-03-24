# from django.shortcuts import render, get_object_or_404
# from .forms import CommentForm
# from exhibition.models import Post


# def post_comment(request, artform, pk):
#     """
#     Add comments to full post
#     """
#     queryset = Post.objects.all()
#     post = get_object_or_404(queryset, pk=pk)
#     comments = post.comments.all().order_by('created_date')
#     template_name = 'comments/add_comment.html'

#     comment_form = CommentForm(data=request.POST)

#     if comment_form.is_valid():
#         comment_form.instance.user_name = request.user
#         comment = comment_form.save(commit=False)
#         comment.post = post
#         comment.save()
#     else:
#         comment_form = CommentForm()

#     context = {
#         'post': post,
#         'comments': comments,
#         'comment_form': CommentForm(),
#     }
#     return render(request, template_name, context)
