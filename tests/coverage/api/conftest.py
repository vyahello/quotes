import pytest
from urequest.session import HttpSession, Session


@pytest.fixture(scope="module")
def session() -> Session:
    with HttpSession() as http_session:  # type: Session
        yield http_session
