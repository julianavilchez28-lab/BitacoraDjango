from django.db import models

class Cancion(models.Model):
    
    CATEGORIA  = [
        ('Pop', 'Pop'),
        ('Rock', 'Rock'),
        ('Hip-Hop', 'Hip-Hop'),
        ('Electrónica', 'Electrónica'),
        ('Reguetón', 'Reguetón'),
        ('Jazz', 'Jazz'),
        ('Clásica', 'Clásica'),
        ('Bachata', 'Bachata'),
        ('Otro', 'Otro'),
    ]
    
    nombre = models.CharField(max_length=100)
    artista = models.CharField(max_length=100)
    genero = models.CharField(max_length=50, choices=CATEGORIA)
    calificacion = models.IntegerField()
    imagen = models.ImageField(upload_to='canciones/', null=True, blank=True)
    
    def __str__(self):
        return self.nombre
    

class Playlist(models.Model):
    nombre = models.CharField(max_length=100)
    canciones = models.ManyToManyField(Cancion)
    descripcion = models.TextField(blank=True)
    
    def __str__(self):
        return self.nombre
# Create your models here.
