import pytest
from selenium.webdriver.remote.webdriver import WebDriver
from tests.coverage.web.helper.pages import EditPage
from tests.markers import web  # noqa: I100

pytestmark = web


@pytest.fixture()
def edit_page(browser: WebDriver) -> EditPage:
    page: EditPage = EditPage(browser, page_id=47)
    if not page.loaded():
        page.navigate()
    yield page


def test_edit_current(edit_page: EditPage) -> None:
    edit_page.form().fill_quote(
        "If your dreams don't scare you, they aren't big enough"
    )
    edit_page.form().fill_author("Muhammad Ali")
    edit_page.form().fill_source(
        "https://www.blackfilm.com/read/2019/04/new-trailer-to-hbos-whats-my-name-muhammad-ali"
    )
    edit_page.form().fill_cover(
        "https://www.blackfilm.com/read/wp-content/uploads/2019/04/Whats-My-Name.jpg"
    )
    assert edit_page.edit().message() == "Quote is updated"
