from django.contrib import admin
from .models import PostLike, PostDislike, CommentLike, CommentDislike

admin.site.register(PostLike)
admin.site.register(PostDislike)
admin.site.register(CommentLike)
admin.site.register(CommentDislike)
