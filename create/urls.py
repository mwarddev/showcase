from django.urls import path
from . import views

urlpatterns = [
    path('profile/', views.profile, name='profile'),
    path('create_post/', views.create_post, name='create_post'),
    path('profile/update_post/<int:pk>/',
         views.update_post,
         name='update_post'),
    path('profile/delete/<int:pk>/', views.delete_post, name='delete'),
]
