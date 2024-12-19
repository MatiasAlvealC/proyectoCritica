"""login URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin  # Importa el módulo para registrar y manejar el panel de administración de Django.
from django.urls import path, include  # Importa los módulos para definir rutas y incluir rutas de otras aplicaciones.

urlpatterns = [  # Lista de las rutas o URLs que el proyecto debe manejar.
    path('', include('core.urls')),  # Incluye las URLs definidas en la aplicación 'core', que maneja la página principal y otras secciones.
    path('admin/', admin.site.urls),  # Ruta para acceder al panel de administración de Django (por defecto en '/admin/').
    path('accounts/', include('django.contrib.auth.urls')),  # Incluye las URLs predeterminadas de autenticación de Django, como login, logout, etc.
]
