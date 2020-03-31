from django.conf import settings
import pytest


@pytest.fixture(autouse=True)  # noqa: PT004
def call_quotes_settings() -> None:  # noqa: PT004, for python >= 3.8.x
    if not settings.configured:
        settings.configure()
