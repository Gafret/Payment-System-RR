from django.apps import AppConfig


class OrgsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "orgs"

    def ready(self):
        from django.db.models.fields import CharField
        from django.db.models.functions import Length

        CharField.register_lookup(Length, "length")
