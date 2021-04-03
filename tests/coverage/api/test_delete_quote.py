import pytest
from tests.markers import api
from urequest.response import Response
from urequest.session import Session
from urequest.url import HttpsUrl

pytestmark = api


@pytest.fixture(scope="module")
def delete_quote_page(session: Session) -> Response:
    yield session.get(
        HttpsUrl(host="quote-quote.herokuapp.com", path="delete/2")
    )


@pytest.fixture(scope="module")
def delete_quote_content(delete_quote_page: Response) -> str:
    yield str(delete_quote_page)


def test_new_quote_status(delete_quote_page: Response) -> None:
    assert delete_quote_page.is_ok()


def test_title(delete_quote_content: str) -> None:
    assert "Delete Quote" in delete_quote_content


def test_navigation(delete_quote_content: str) -> None:
    assert "Delete" in delete_quote_content
    assert "Go Back" in delete_quote_content
