"""Module represents API for applications."""
from django.apps import AppConfig


class QuotesConfig(AppConfig):
    """Main `app` application configuration."""

    name: str = "app"
