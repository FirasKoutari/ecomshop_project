from django.apps import AppConfig
from django.apps import AppConfig





class CartappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'CartApp'


class CartAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'CartApp'

    def ready(self):
        import CartApp.signals