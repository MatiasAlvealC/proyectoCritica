from django.urls import path
from core import views


urlpatterns = [
    path('', views.home, name='home'),
    path('pelicula/<int:pelicula_id>/', views.pelicula_detalles, name='pelicula_detalles'),
    path('accion_aventura/', views.accion_aventura, name='accion_aventura'),
    path('comedia/', views.comedia, name='comedia'),
    path('drama/', views.drama, name='drama'),
    path('ciencia_fantasia/', views.ciencia_fantasia, name='ciencia_fantasia'),
    path('horror_suspenso/', views.horror_suspenso, name='horror_suspenso'),
    path('romance/', views.romance, name='romance'),
    path('animacion/', views.animacion, name='animacion'),
    path('documental/', views.documental, name='documental'),
    path('nosotros/', views.nosotros, name='nosotros'),
    path('contacto/', views.contacto, name='contacto'),
]