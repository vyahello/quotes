"""Contains API for apps."""
from django.apps import AppConfig


class ApiConfig(AppConfig):
    """API configuration."""

    name: str = "api"
