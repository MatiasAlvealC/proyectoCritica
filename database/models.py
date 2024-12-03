from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User

# Modelo para las Categorías
class Categoria(models.Model):
  nombre = models.CharField(max_length=100, verbose_name="Nombre")
  created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
  updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

  class Meta:
    verbose_name = "categoría"
    verbose_name_plural = "categorías"

  def __str__(self):
    return self.nombre


# Modelo de Película
class Pelicula(models.Model):
  titulo = models.CharField(max_length=100)
  sinopsis = models.TextField()
  fecha_estreno = models.DateField()
  duracion = models.IntegerField(help_text="Duración en minutos")
  director = models.CharField(max_length=100)
  image = models.ImageField(upload_to='images/', default='images/default.jpg')
  genero = models.ManyToManyField(Categoria, through='PeliculaCategoria', verbose_name="Categorías")
  created = models.DateTimeField(auto_now_add=True)
  updated = models.DateTimeField(auto_now=True)

  class Meta:
    verbose_name = "película"
    verbose_name_plural = "películas"

  def __str__(self):
    return self.titulo


# Tabla intermedia personalizada para Películas y Categorías
class PeliculaCategoria(models.Model):
  pelicula = models.ForeignKey(Pelicula, on_delete=models.CASCADE)
  categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
  fecha_asignacion = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de asignación")

  class Meta:
    verbose_name = "relación película-categoría"
    verbose_name_plural = "relaciones película-categoría"
    unique_together = ('pelicula', 'categoria')

  def __str__(self):
    return f"{self.pelicula.titulo} - {self.categoria.nombre}"


# Modelo para Comentarios
class Comentario(models.Model):
  pelicula = models.ForeignKey(Pelicula, on_delete=models.CASCADE, related_name="comentarios", verbose_name="Película")
  usuario = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Usuario")
  texto = models.TextField(verbose_name="Comentario")
  fecha_creacion = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")

  class Meta:
    verbose_name = "comentario"
    verbose_name_plural = "comentarios"
    ordering = ['-fecha_creacion']

  def __str__(self):
    return f"Comentario de {self.usuario.username} en {self.pelicula.titulo}"
