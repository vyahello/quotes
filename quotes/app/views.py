"""Module represents API for routes."""
from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Quote


def quotes(request: WSGIRequest) -> HttpResponse:
    """Returns list of all quotes.

    Args:
        request (WSGIRequest): user request
    """
    return render(request, "quotes/quotes.html", {"quotes": Quote.objects.all()})  # pylint:disable=no-member


def detail_quote(request: WSGIRequest, primary_key: int) -> HttpResponse:
    """Returns list of all quotes.

    Args:
        request (WSGIRequest): user request
        primary_key (int): id number of a quote
    """
    return render(request, "quotes/detail_quote.html", {"quote": get_object_or_404(Quote, pk=primary_key)})


def new_quote(request: WSGIRequest) -> HttpResponse:
    """Creates a new quote.

    Args:
        request (WSGIRequest): user request
    """


def edit_quote(request: WSGIRequest, primary_key: int) -> HttpResponse:
    """Edits a single quote.

    Args:
        request (WSGIRequest): user request
        primary_key (int): id number of a quote
    """


def delete_quote(request: WSGIRequest, primary_key: int) -> HttpResponse:
    """Deletes a single quote.

    Args:
        request (WSGIRequest): user request
        primary_key (int): id number of a quote
    """
