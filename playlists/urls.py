from django.urls import path
from . import views

urlpatterns = [
    path('', views.playlist_list, name='playlist_list'),
    path('create/', views.playlist_create, name='playlist_create'),
]