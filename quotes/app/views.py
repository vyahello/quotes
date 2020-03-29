"""Module represents API for routes."""
from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse
from django.shortcuts import render
from .models import Quote


def quotes(request: WSGIRequest) -> HttpResponse:
    """Returns list of all quotes.

    Args:
        request (WSGIRequest): user request
    """
    return render(request, "quotes/quotes.html", {"quotes": Quote.objects.all()})  # pylint:disable=no-member
