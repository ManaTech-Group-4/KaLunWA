from django.apps import AppConfig

class PageContainersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'kalunwa.page_containers'

    def ready(self) -> None:
        import kalunwa.page_containers.signals
        return super().ready()
