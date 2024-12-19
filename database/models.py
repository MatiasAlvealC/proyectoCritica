from django.db import models  # Importa el módulo models para definir los modelos de base de datos.
from django.utils.timezone import now  # Importa now para trabajar con fechas y horas.
from django.contrib.auth.models import User  # Importa el modelo User para asociar los comentarios con los usuarios.

# Modelo para las Categorías
class Categoria(models.Model):  # Define el modelo de la categoría.
    nombre = models.CharField(max_length=100, verbose_name="Nombre")  # Campo para el nombre de la categoría.
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")  # Fecha de creación.
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")  # Fecha de última edición.

    class Meta:
        verbose_name = "categoría"  # Define el nombre singular del modelo.
        verbose_name_plural = "categorías"  # Define el nombre plural del modelo.

    def __str__(self):
        return self.nombre  # Representación en forma de cadena del modelo.

# Modelo de Película
class Pelicula(models.Model):  # Define el modelo de la película.
    titulo = models.CharField(max_length=100)  # Título de la película.
    sinopsis = models.TextField()  # Sinopsis de la película.
    fecha_estreno = models.DateField()  # Fecha de estreno.
    duracion = models.IntegerField(help_text="Duración en minutos")  # Duración en minutos.
    director = models.CharField(max_length=100)  # Nombre del director.
    image = models.ImageField(upload_to='images/', default='images/default.jpg')  # Imagen de la película.
    genero = models.ManyToManyField(Categoria, through='PeliculaCategoria', verbose_name="Categorías")  # Relación con las categorías.
    created = models.DateTimeField(auto_now_add=True)  # Fecha de creación de la película.
    updated = models.DateTimeField(auto_now=True)  # Fecha de última edición.

    class Meta:
        verbose_name = "película"  # Define el nombre singular del modelo.
        verbose_name_plural = "películas"  # Define el nombre plural del modelo.

    def __str__(self):
        return self.titulo  # Representación en forma de cadena del modelo.

# Tabla intermedia personalizada para Películas y Categorías
class PeliculaCategoria(models.Model):  # Modelo para la relación entre películas y categorías.
    pelicula = models.ForeignKey(Pelicula, on_delete=models.CASCADE)  # Relación con la película.
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)  # Relación con la categoría.
    fecha_asignacion = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de asignación")  # Fecha de asignación.

    class Meta:
        verbose_name = "relación película-categoría"  # Nombre singular del modelo.
        verbose_name_plural = "relaciones película-categoría"  # Nombre plural del modelo.
        unique_together = ('pelicula', 'categoria')  # Asegura que la misma película no esté en la misma categoría más de una vez.

    def __str__(self):
        return f"{self.pelicula.titulo} - {self.categoria.nombre}"  # Representación de la relación.

# Modelo para Comentarios
class Comentario(models.Model):  # Modelo para los comentarios de las películas.
    pelicula = models.ForeignKey(Pelicula, on_delete=models.CASCADE, related_name="comentarios", verbose_name="Película")  # Relación con la película.
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Usuario")  # Relación con el usuario que comenta.
    texto = models.TextField(verbose_name="Comentario")  # Texto del comentario.
    fecha_creacion = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")  # Fecha de creación del comentario.

    class Meta:
        verbose_name = "comentario"  # Nombre singular del modelo.
        verbose_name_plural = "comentarios"  # Nombre plural del modelo.
        ordering = ['-fecha_creacion']  # Ordenar los comentarios por fecha de creación de manera descendente.

    def __str__(self):
        return f"Comentario de {self.usuario.username} en {self.pelicula.titulo}"  # Representación del comentario.
