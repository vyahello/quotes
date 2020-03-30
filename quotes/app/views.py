"""Module represents API for routes."""
from typing import Any, Dict
from django.contrib import messages
from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from .forms import QuoteForm
from .models import Quote


def __fill_new_form(request: WSGIRequest, form: QuoteForm, message: str, context: Dict[str, Any]) -> HttpResponse:
    """Fills fresh quote form.

    Args:
        request (WSGIRequest): user request
        form (QuoteForm): user form
        message (str): output message
        context (dict): data
    """
    if form.is_valid():
        form.save()
        messages.success(request, message)
        return redirect(to="quotes:quotes")
    return render(request, template_name="quotes/new_quote.html", context=context)


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
    return __fill_new_form(request, form, message="Quote is added", context={"form": form})


def edit_quote(request: WSGIRequest, primary_key: int) -> HttpResponse:
    """Edits a single quote.

    Args:
        request (WSGIRequest): user request
        primary_key (int): id number of a quote
    """
    quote: Quote = get_object_or_404(Quote, pk=primary_key)
    form: QuoteForm = QuoteForm(request.POST or None, instance=quote)
    return __fill_new_form(request, form, message="Quote is updated", context={"quote": quote, "form": form})


def delete_quote(request: WSGIRequest, primary_key: int) -> HttpResponse:
    """Deletes a single quote.

    Args:
        request (WSGIRequest): user request
        primary_key (int): id number of a quote
    """
    quote: Quote = get_object_or_404(Quote, pk=primary_key)
    if request.method == "POST":
        quote.delete()
        messages.success(request, message="Quote is deleted")
        return redirect(to="quotes:quotes")
    return render(request, template_name="quotes/delete_quote.html", context={"quote": quote})
