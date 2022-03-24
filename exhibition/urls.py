from django.urls import path
from . import views

urlpatterns = [
    path('posts/<str:artform>/', views.get_posts, name='artform'),
    path('posts/<str:artform>/<int:pk>/',
         views.get_full_post,
         name='full_post'),
    # path('posts/<str:artform>/<int:pk>/comment/<int:comment_id>',
    #      views.edit_comment,
    #      name='update_comment'),
]
