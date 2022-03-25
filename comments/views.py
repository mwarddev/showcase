# from django.shortcuts import render, redirect, get_object_or_404
# from django.http import HttpResponseRedirect
# # from .forms import CommentForm
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

# def delete_comment(request, pk, comment_id):
#     """
#     Delete a comment
#     """
#     post = get_object_or_404(Post, pk=pk)
#     comments = post.comments.all()
#     comment_to_delete = comments.filter(pk=comment_id)
#     template_name = 'comments/delete_comment.html'

#     # if request.method == 'GET':
#     #     previous_page = request.META.get('HTTP_REFERER')
#     #     print('URL =' + previous_page)    

#     if request.method == 'POST':
#         comment_to_delete.delete()

#         return redirect('../../../')
#         # return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
#     context = {
#         'comment_to_delete': comment_to_delete
#     }

#     return render(request, template_name, context)
