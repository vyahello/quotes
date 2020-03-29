"""Represents URL endpoints for an application."""
from typing import Any, List
from django.urls import path
from . import views


app_name: str = "quotes"
urlpatterns: List[Any] = [path("", views.quotes, name="quotes")]
