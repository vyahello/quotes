"""Represents URL endpoints for an application."""
from typing import Any, List
from django.urls import path
from .views import QuoteList

urlpatterns: List[Any] = [path("", QuoteList.as_view())]
