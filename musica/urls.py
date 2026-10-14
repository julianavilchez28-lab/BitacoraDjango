from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('agregar/', views.agregar_cancion, name='agregar_cancion'),
    path('playlists/', views.ver_playlists, name='ver_playlists'),
    path('playlists/crear/', views.crear_playlist, name='crear_playlist'),
]