"""Represents REST permissions for an application."""
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import BasePermission, SAFE_METHODS
from rest_framework.request import Request
from app.models import Quote


class IsOwnerOrReadOnly(BasePermission):
    """Make sure only owners of quotes can edit them."""

    def has_object_permission(self, request: Request, _: GenericAPIView, obj: Quote) -> bool:  # noqa: U101
        """Checks in objects has appropriate permissions."""
        return True if request.method in SAFE_METHODS else obj.user == request.user
