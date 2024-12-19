"""
WSGI config for proyectoCritica project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/
"""

import os  # Importa el módulo os para interactuar con el sistema operativo.

from django.core.wsgi import get_wsgi_application  # Importa la función para obtener la aplicación WSGI de Django.

# Establece el archivo de configuración de Django (settings) a utilizar.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'proyectoCritica.settings')

# Crea la aplicación WSGI utilizando la configuración establecida.
application = get_wsgi_application()
