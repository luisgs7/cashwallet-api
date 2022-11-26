"""Config Django App user"""
from django.apps import AppConfig


class UserConfig(AppConfig):
    """Class config for django app user"""
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'user'
