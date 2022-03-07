from django.urls import path
from . import views

urlpatterns = [
    path('', views.CategorySelect.as_view(), name='home'),
    path('posts/<str:artform>/', views.SelectedCategory.as_view(), name='artform'),
    path('<str:slug>/', views.FullPostView.as_view(), name='full_post'),
]
