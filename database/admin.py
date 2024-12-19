from django.contrib import admin  # Importa la función admin para registrar modelos en el panel de administración.
from .models import Pelicula, Categoria, PeliculaCategoria, Comentario  # Importa los modelos que se van a registrar.

admin.site.register(Pelicula)  # Registra el modelo Pelicula en el panel de administración.
admin.site.register(Categoria)  # Registra el modelo Categoria en el panel de administración.
admin.site.register(PeliculaCategoria)  # Registra el modelo PeliculaCategoria en el panel de administración.
admin.site.register(Comentario)  # Registra el modelo Comentario en el panel de administración.
