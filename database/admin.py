from django.contrib import admin
from .models import Pelicula, Categoria, PeliculaCategoria, Comentario

admin.site.register(Pelicula)
admin.site.register(Categoria)
admin.site.register(PeliculaCategoria)
admin.site.register(Comentario)