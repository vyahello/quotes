"""Represents URL endpoints for an application."""
from typing import Any, List
from django.urls import include, path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from .views import QuoteDetail, Quotes


urlpatterns: List[Any] = [
    path("", Quotes.as_view()),
    path("<int:pk>", QuoteDetail.as_view()),
    path("api-auth/", include("rest_framework.urls")),
    path(
        "docs/",
        get_schema_view(
            openapi.Info(
                title="Quotes REST API",
                default_version="v1",
                description="Swagger documentation for Quotes REST API",
                terms_of_service="https://www.google.com/policies/terms/",
                contact=openapi.Contact(email="vyahello@gmail.com"),
                license=openapi.License(name="MIT License"),
            ),
            public=True,
            permission_classes=(permissions.AllowAny,),
        ).with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
]
