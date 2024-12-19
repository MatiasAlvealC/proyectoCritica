"""
ASGI config for login project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/asgi/
"""

import os  # Importa el módulo os para interactuar con el sistema operativo, como establecer variables de entorno.

from django.core.asgi import get_asgi_application  # Importa la función get_asgi_application desde django.core.asgi para obtener la aplicación ASGI.

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'login.settings')  # Establece la variable de entorno DJANGO_SETTINGS_MODULE, que le dice a Django qué archivo de configuración usar. 

application = get_asgi_application()  # Obtiene la aplicación ASGI de Django, que es utilizada para la comunicación en tiempo real y soporte de WebSockets.

