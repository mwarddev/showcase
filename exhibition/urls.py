from django.urls import path
from . import views


urlpatterns = [
    path('posts/<str:artform>/', views.get_posts, name='artform'),
    path('posts/<str:artform>/<int:pk>/',
         views.get_full_post,
         name='full_post'),
    # path('', include('comments.urls'), name='comments-urls'),
    path('posts/<str:artform>/<int:pk>/<int:comment_id>/',
         views.delete_comment,
         name='delete_comment'),
]
