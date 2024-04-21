from django.apps import AppConfig

class XlinkConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "xlink"
    def ready(self):
        import xlink.signals 