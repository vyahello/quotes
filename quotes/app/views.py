"""Module represents API for routes."""
from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse


def index(_: WSGIRequest) -> HttpResponse:
    """Renders home page."""
    return HttpResponse("Welcome to Django")
