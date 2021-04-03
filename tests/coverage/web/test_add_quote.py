import pytest
from selenium.webdriver.remote.webdriver import WebDriver
from tests.coverage.web.helper.pages import NewPage
from tests.markers import web  # noqa: I100

pytestmark = web


@pytest.fixture()
def new_page(browser: WebDriver) -> NewPage:
    page: NewPage = NewPage(browser)
    if not page.loaded():
        page.navigate()
    yield page


def test_new_quote(new_page: NewPage) -> None:
    new_page.form().fill_quote(
        "If your dreams don't scare you, they aren't big enough"
    )
    new_page.form().fill_author("Muhammad Ali")
    new_page.form().fill_source(
        "https://www.blackfilm.com/read/2019/04/new-trailer-to-hbos-whats-my-name-muhammad-ali"
    )
    new_page.form().fill_cover(
        "https://www.blackfilm.com/read/wp-content/uploads/2019/04/Whats-My-Name.jpg"
    )
    assert new_page.new().message() == "Quote is added"
