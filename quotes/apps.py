"""Module represents API for applications."""
from django.apps import AppConfig


class QuotesConfig(AppConfig):
    """Main `quotes` application configuration."""

    name: str = "quotes"
