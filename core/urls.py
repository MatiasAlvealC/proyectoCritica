from django.urls import path, include  # Importa las funciones necesarias para definir rutas en Django.
from core import views  # Importa las vistas del módulo core.
from django.contrib.auth.views import LogoutView  # Importa la vista de cierre de sesión de Django.

urlpatterns = [  # Lista de las rutas URL que la aplicación gestionará.
    path('', views.home, name='home'),  # Ruta para la página de inicio.
    path('register/', views.register, name='register'),  # Ruta para la página de registro de usuarios.
    path('login/', views.user_login, name='login'),  # Ruta para la página de inicio de sesión.
    path('logout/', LogoutView.as_view(), name='logout'),  # Ruta para cerrar sesión utilizando la vista integrada de Django.
    path('pelicula/<int:pelicula_id>/', views.pelicula_detalles, name='pelicula_detalles'),  # Ruta para ver los detalles de una película.
    path('accion_aventura/', views.accion_aventura, name='accion_aventura'),  # Ruta para la categoría de Acción/Aventura.
    path('comedia/', views.comedia, name='comedia'),  # Ruta para la categoría de Comedia.
    path('drama/', views.drama, name='drama'),  # Ruta para la categoría de Drama.
    path('ciencia_fantasia/', views.ciencia_fantasia, name='ciencia_fantasia'),  # Ruta para la categoría de Ciencia Ficción.
    path('horror_suspenso/', views.horror_suspenso, name='horror_suspenso'),  # Ruta para la categoría de Horror/Suspenso.
    path('romance/', views.romance, name='romance'),  # Ruta para la categoría de Romance.
    path('animacion/', views.animacion, name='animacion'),  # Ruta para la categoría de Animación.
    path('documental/', views.documental, name='documental'),  # Ruta para la categoría de Documentales.
    path('nosotros/', views.nosotros, name='nosotros'),  # Ruta para la página "Nosotros".
    path('contacto/', views.contacto, name='contacto'),  # Ruta para la página de contacto.
    path('pelicula/<int:pelicula_id>/comentar/', views.comentar, name='comentar'),  # Ruta para comentar sobre una película.
]
