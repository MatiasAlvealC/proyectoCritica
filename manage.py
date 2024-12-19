#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os  # Importa el módulo os para interactuar con el sistema operativo.
import sys  # Importa el módulo sys para trabajar con argumentos de línea de comandos.

def main():
    """Ejecuta tareas administrativas de Django."""
    
    # Establece la variable de entorno que indica el archivo de configuración de Django a usar.
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'proyectoCritica.settings')
    
    try:
        # Intenta importar la función 'execute_from_command_line' de Django, que permite ejecutar comandos desde la línea de comandos.
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        # Si ocurre un error de importación, lanza una excepción personalizada.
        raise ImportError(
            "No se pudo importar Django. ¿Estás seguro de que está instalado y "
            "disponible en tu variable de entorno PYTHONPATH? ¿Olvidaste activar un entorno virtual?"
        ) from exc
    
    # Ejecuta el comando pasado por línea de comandos (sys.argv).
    execute_from_command_line(sys.argv)


# Si el script se ejecuta directamente, llama a la función main().
if __name__ == '__main__':
    main()
