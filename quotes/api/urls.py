"""Represents URL endpoints for an application."""
from typing import Any, List
from django.urls import path
from .views import Quotes

urlpatterns: List[Any] = [path("", Quotes.as_view())]
