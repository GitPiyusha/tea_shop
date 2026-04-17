from django.apps import AppConfig


class TeashopConfig(AppConfig):
    name = 'teaShop'

    def ready(self):
        import teaShop.signals