from django.apps import AppConfig


class ArticlesAppConfig(AppConfig):
    name = 'Djangoapi.apps.articles'
    label = 'articles'
    verbose_name = 'Articles'

    def ready(self):
        import Djangoapi.apps.articles.signals

default_app_config = 'Djangoapi.apps.articles.ArticlesAppConfig'
