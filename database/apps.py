from django.apps import AppConfig  # Importa AppConfig, la clase base para configurar las aplicaciones en Django.

class DatabaseConfig(AppConfig):  # Define una clase DatabaseConfig para configurar la aplicación "database".
    default_auto_field = 'django.db.models.BigAutoField'  # Especifica el tipo de campo por defecto para las claves primarias (BigAutoField).
    name = 'database'  # Define el nombre de la aplicación como 'database'.
