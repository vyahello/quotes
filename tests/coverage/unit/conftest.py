import pytest
from django.conf import settings


@pytest.fixture(autouse=True)
def call_quotes_settings() -> None:
    if not settings.configured:
        settings.configure()
