import pytest
from selenium.webdriver.remote.webdriver import WebDriver
from tests.coverage.web.helper.pages import DeletePage
from tests.markers import web  # noqa: I100

pytestmark = web


@pytest.fixture()
def delete_page(browser: WebDriver) -> DeletePage:
    page: DeletePage = DeletePage(browser)
    if not page.loaded():
        page.navigate()
    yield page


def test_delete_recent(delete_page: DeletePage) -> None:
    assert delete_page.delete().message() == "Quote is deleted"
