from django.urls import path, include
from . import views

urlpatterns = [
    path('profile/', views.profile, name='profile'),
    path('create_post/', views.create_post, name='create_post'),
    path('', include('exhibition.urls'), name='exhibition-urls'),
]