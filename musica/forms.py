from django import forms 
from .models import Cancion, Playlist

class CancionForm(forms.ModelForm):
    class Meta:
        model = Cancion
        fields = ['nombre', 'artista', 'genero', 'calificacion', 'imagen']
        
        
class PlaylistForm(forms.ModelForm):
    class Meta:
        model = Playlist
        fields = ['nombre', 'canciones', 'descripcion']