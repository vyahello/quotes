from quotes.manager.settings import STATIC_URL, ROOT_URLCONF, INSTALLED_APPS, WSGI_APPLICATION, STATICFILES_DIRS
from tests.markers import unit

pytestmark = unit


def test_app() -> None:
    assert "app" in INSTALLED_APPS


def test_wsgi_application() -> None:
    assert WSGI_APPLICATION == "manager.wsgi.application"


def test_root_url_conf():
    assert ROOT_URLCONF == "manager.urls"


def test_static_url():
    assert STATIC_URL == "/static/"


def test_static_files_dirs():
    assert "static" in STATICFILES_DIRS[0]
