import pytest
from tests.markers import api
from urequest.response import Response
from urequest.session import Session
from urequest.url import Address

pytestmark = api


@pytest.fixture(scope="module")
def home_page(session: Session, home_url: Address) -> Response:
    yield session.get(home_url)


@pytest.fixture(scope="module")
def home_content(home_page: Response) -> str:
    yield str(home_page)


def test_home_status(home_page: Response) -> None:
    assert home_page.is_ok()


def test_title(home_content: str) -> None:
    assert "Quotes" in home_content


def test_record_table(home_content: str) -> None:
    assert "Quote" in home_content
    assert "Author" in home_content
    assert "Added" in home_content
    assert "Edit Quote" in home_content
    assert "Delete" in home_content


def test_navigation(home_content: str) -> None:
    assert "About" in home_content
    assert "Login" in home_content
    assert "Add a quote" in home_content
