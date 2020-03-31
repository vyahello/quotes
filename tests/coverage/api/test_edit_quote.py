import pytest
from tests.markers import api
from urequest.response import Response
from urequest.session import Session
from urequest.url import HttpsUrl

pytestmark = api


@pytest.fixture(scope="module")
def edit_quote_page(session: Session) -> Response:
    yield session.get(HttpsUrl(host="quote-quote.herokuapp.com", path="edit/3"))


@pytest.fixture(scope="module")
def edit_quote_content(edit_quote_page: Response) -> str:
    yield str(edit_quote_page)


def test_edit_quote_status(edit_quote_page: Response) -> None:
    assert edit_quote_page.is_ok()


def test_title(edit_quote_content: str) -> None:
    assert "Edit Quote" in edit_quote_content


def test_fields_to_fill(edit_quote_content: str) -> None:
    assert "Quote" in edit_quote_content
    assert "Author" in edit_quote_content
    assert "Source" in edit_quote_content
    assert "Cover" in edit_quote_content


def test_navigation(edit_quote_content: str) -> None:
    assert "Edit" in edit_quote_content
    assert "Go Back" in edit_quote_content
