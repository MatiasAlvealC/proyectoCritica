from django.urls import path, include
from core import views
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
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