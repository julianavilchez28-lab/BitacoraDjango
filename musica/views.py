from django.shortcuts import render, redirect
from .models import Cancion, Playlist
from .forms import CancionForm, PlaylistForm

def inicio(request):
    canciones = Cancion.objects.all()
    
    buscar = request.GET.get('buscar')
    if buscar:
        canciones = Cancion.objects.filter(nombre__icontains=buscar)
        
    return render(request, 'musica/inicio.html', {'canciones': canciones})
        

def agregar_cancion(request):
    if request.method == 'POST':
        form = CancionForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('inicio')
    else:
        form = CancionForm()
    return render(request, 'musica/agregar_cancion.html', {'form': form})

def crear_playlist(request):
    if request.method == 'POST':
        form = PlaylistForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ver_playlists')
    else:
        form = PlaylistForm()
    return render(request, 'musica/crear_playlist.html', {'form': form})

def ver_playlists(request):
    playlists = Playlist.objects.all()
    
    return render(request, 'musica/playlists.html', {'playlists': playlists})
# Create your views here.
