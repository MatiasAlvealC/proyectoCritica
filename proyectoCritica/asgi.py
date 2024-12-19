"""
ASGI config for proyectoCritica project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/asgi/
"""

import os  # Importa el módulo 'os' para interactuar con el sistema operativo.

from django.core.asgi import get_asgi_application  # Importa la función para obtener la aplicación ASGI de Django.

# Establece la variable de entorno 'DJANGO_SETTINGS_MODULE' para indicar qué archivo de configuración usar.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'proyectoCritica.settings')

application = get_asgi_application()  # Obtiene la aplicación ASGI de Django que se utilizará para desplegar el proyecto.
