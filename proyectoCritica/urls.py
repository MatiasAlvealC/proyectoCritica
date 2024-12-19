"""proyectoCritica URL Configuration

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
from django.contrib import admin  # Importa el módulo para el admin de Django.
from django.urls import path, include  # Importa los módulos para definir rutas de URLs.
from django.conf import settings  # Importa la configuración de Django.


# Definición de las URLs del proyecto.
urlpatterns = [
    path('admin/', admin.site.urls),  # Ruta para acceder al panel de administración de Django.
    path('', include('core.urls')),  # Incluye las rutas definidas en la aplicación 'core'.
]

# Si el modo DEBUG está activado (para desarrollo).
if settings.DEBUG:
    from django.conf.urls.static import static  # Importa el módulo para manejar archivos estáticos en desarrollo.
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  # Añade la configuración de archivos multimedia.
