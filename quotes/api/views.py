"""Module represents API for routes."""
from typing import List, Type
from rest_framework.generics import ListCreateAPIView
from app.models import Quote  # pylint: disable=import-error
from .serializers import QuoteSerializer


class QuoteList(ListCreateAPIView):
    """Represents a quote list route."""

    queryset: List[Quote] = Quote.objects.all()
    serializer_class: Type[QuoteSerializer] = QuoteSerializer
