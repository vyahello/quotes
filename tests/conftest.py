from _pytest.config.argparsing import Parser
from _pytest.fixtures import SubRequest
from django.conf import settings
import pytest
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.webdriver import WebDriver
from urequest.session import HttpSession, Session
from urequest.url import Address, HttpsUrl


@pytest.fixture(autouse=True)  # noqa: PT004
def call_quotes_settings() -> None:  # noqa: PT004, for python >= 3.8.x
    if not settings.configured:
        settings.configure()


@pytest.fixture(scope="module")
def session() -> Session:
    with HttpSession() as http_session:  # type: Session
        yield http_session


@pytest.fixture(scope="module")
def home_url() -> Address:
    yield HttpsUrl("quote-quote.herokuapp.com")


@pytest.fixture()
def browser(request: SubRequest) -> WebDriver:
    options: Options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    chrome: WebDriver = Chrome(
        request.config.getoption("--chrome-path"), chrome_options=options
    )
    yield chrome
    chrome.quit()


def pytest_addoption(parser: Parser) -> None:
    """Adds additional (API) command line arguments."""
    parser.addoption(
        "--chrome-path",
        action="store",
        help="chromedriver executable path e.g '/path/to/chromedriver'",
        type=str,
        default="/usr/local/bin/chromedriver",
    )
