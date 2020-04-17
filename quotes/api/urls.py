"""Represents URL endpoints for an application."""
from typing import Any, List
from django.urls import include, path
from .views import QuoteDetail, Quotes

urlpatterns: List[Any] = [
    path("", Quotes.as_view()),
    path("<int:pk>", QuoteDetail.as_view()),
    path("api-auth/", include("rest_framework.urls")),
]
