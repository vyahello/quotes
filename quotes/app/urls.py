"""Represents URL endpoints for an application."""
from typing import Any, List
from django.urls import path
from .views import delete_quote, detail_quote, edit_quote, new_quote, quotes


app_name: str = "quotes"
urlpatterns: List[Any] = [
    path("", quotes, name="quotes"),
    path("<int:primary_key>", detail_quote, name="detail_quote"),
    path("new", new_quote, name="new_quote"),
    path("edit/<int:primary_key>", edit_quote, name="edit_quote"),
    path("delete/<int:primary_key>", delete_quote, name="delete_quote"),
]
