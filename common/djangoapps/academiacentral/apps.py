from django.apps import AppConfig


class AcademiaCentralConfig(AppConfig):
    name = 'common.djangoapps.academiacentral'
    verbose_name = 'Academia Central Helpers'

    def ready(self):
        # Connect signal handlers.
        from .signals import receivers  # pylint: disable=unused-import

