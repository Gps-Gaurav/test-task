from django.apps import AppConfig

# Shared app ka config (usually common models ke liye)
class SharedConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'shared'
