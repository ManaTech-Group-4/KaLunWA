from django.apps import AppConfig


class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'kalunwa.users'

    def ready(self) -> None:
        import kalunwa.users.signals
        return super().ready()