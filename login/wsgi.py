"""
WSGI config for login project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/
"""

import os  # Importa el módulo 'os' para interactuar con el sistema operativo.

from django.core.wsgi import get_wsgi_application  # Importa la función para obtener la aplicación WSGI de Django.

# Establece la variable de entorno 'DJANGO_SETTINGS_MODULE' para indicar qué archivo de configuración usar.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'login.settings')

application = get_wsgi_application()  # Obtiene la aplicación WSGI de Django que se utilizará para desplegar el proyecto.
