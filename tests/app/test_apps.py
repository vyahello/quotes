from quotes.app.apps import QuotesConfig
from tests.markers import unit

pytestmark = unit


def test_config() -> None:
    assert QuotesConfig.name == "app"
