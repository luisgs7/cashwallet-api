'''Config Django App "core"'''
from django.apps import AppConfig


class CoreConfig(AppConfig):
    '''app settings'''
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'core'
