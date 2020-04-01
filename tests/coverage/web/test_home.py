import pytest
from selenium.webdriver.remote.webdriver import WebDriver
from tests.coverage.web.helper.pages import HomePage
from tests.markers import web  # noqa: I100

pytestmark = web


@pytest.fixture()
def home_page(browser: WebDriver) -> HomePage:
    page: HomePage = HomePage(browser)
    if not page.loaded():
        page.navigate()
    yield page


def test_title(home_page: HomePage) -> None:
    assert home_page.title() == "Quotes"


def test_add_quote_button(home_page: HomePage) -> None:
    assert home_page.add_quote_button_displayed()


def test_about_button(home_page: HomePage) -> None:
    assert home_page.about_button_displayed()


def test_login_button(home_page: HomePage) -> None:
    assert home_page.login_button_displayed()
