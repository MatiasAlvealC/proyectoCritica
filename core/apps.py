from django.apps import AppConfig  # Importa AppConfig desde django.apps para configurar una aplicación en Django.

class CoreConfig(AppConfig):  # Define una clase CoreConfig que configura la aplicación 'core'.
    default_auto_field = 'django.db.models.BigAutoField'  # Establece el tipo de campo por defecto para los IDs (claves primarias) como BigAutoField.
    name = 'core'  # Define el nombre de la aplicación, en este caso 'core'.
