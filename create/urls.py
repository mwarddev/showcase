from django.urls import path, include
from . import views

urlpatterns = [
    path('profile/<str:username>/', views.profile, name='profile'),
    path('', include('exhibition.urls'), name='exhibition-urls'),
]