"""Represents URL endpoints for an application."""
from typing import Any, List
from django.urls import path, include
from .views import Quotes, QuoteDetail

urlpatterns: List[Any] = [
    path("", Quotes.as_view()),
    path("<int:pk>", QuoteDetail.as_view()),
    path("api-auth/", include("rest_framework.urls")),
]
