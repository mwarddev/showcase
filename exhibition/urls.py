from django.urls import path
from . import views

urlpatterns = [
    # path('', views.CategorySelect.as_view(), name='home'),
    path('posts/<str:artform>/', views.get_posts, name='artform'),
    # path('posts/<str:artform>/', views.SelectedCategory.as_view(), name='artform'),
    path('posts/<str:artform>/<int:pk>/', views.get_full_post, name='full_post'),
    # path('posts/<str:artform>/<str:slug>/', views.FullPostView.as_view(), name='full_post'),
]
