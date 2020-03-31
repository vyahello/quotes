import pytest
from tests.markers import api
from urequest.response import Response
from urequest.session import Session
from urequest.url import HttpsUrl

pytestmark = api


@pytest.fixture(scope="module")
def new_quote_page(session: Session) -> Response:
    yield session.get(HttpsUrl(host="quote-quote.herokuapp.com", path="new"))


@pytest.fixture(scope="module")
def new_quote_content(new_quote_page: Response) -> str:
    yield str(new_quote_page)


def test_new_quote_status(new_quote_page: Response) -> None:
    assert new_quote_page.is_ok()


def test_title(new_quote_content: str) -> None:
    assert "New Quote" in new_quote_content


def test_fields_to_fill(new_quote_content: str) -> None:
    assert "Quote" in new_quote_content
    assert "Author" in new_quote_content
    assert "Source" in new_quote_content
    assert "Cover" in new_quote_content


def test_navigation(new_quote_content: str) -> None:
    assert "New" in new_quote_content
    assert "Go Back" in new_quote_content
