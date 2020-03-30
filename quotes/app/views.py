"""Module represents API for routes."""
from django.contrib import messages
from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import Quote
from .forms import QuoteForm


def quotes(request: WSGIRequest) -> HttpResponse:
    """Returns list of all quotes.

    Args:
        request (WSGIRequest): user request
    """
    return render(
        request,
        template_name="quotes/quotes.html",
        context={"quotes": Quote.objects.all()},  # pylint:disable=no-member
    )


def detail_quote(request: WSGIRequest, primary_key: int) -> HttpResponse:
    """Returns list of all quotes.

    Args:
        request (WSGIRequest): user request
        primary_key (int): id number of a quote
    """
    return render(
        request, template_name="quotes/detail_quote.html", context={"quote": get_object_or_404(Quote, pk=primary_key)}
    )


def new_quote(request: WSGIRequest) -> HttpResponse:
    """Creates a new quote.

    Args:
        request (WSGIRequest): user request
    """
    form: QuoteForm = QuoteForm(data=request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, message="Added quote")
        return redirect(to="quotes:quotes")
    return render(request, template_name="quotes/new_quote.html", context={"form": form})


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
