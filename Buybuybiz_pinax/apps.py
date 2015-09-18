from importlib import import_module

from django.apps import AppConfig as BaseAppConfig


class AppConfig(BaseAppConfig):

    name = "Buybuybiz_pinax"

    def ready(self):
        import_module("Buybuybiz_pinax.receivers")
