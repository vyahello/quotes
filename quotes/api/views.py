"""Module represents API for routes."""
from typing import List, Type
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from app.models import Quote
from .serializers import QuoteSerializer
from .permissions import IsOwnerOrReadOnly


class Quotes(ListCreateAPIView):
    """Responsible for retrieving all quotes from an application.

    Endpoint is `/api/`

    ``GET``: retrieve all quotes

    ``POST``: creates a new quote
    """

    queryset: List[Quote] = Quote.objects.all()
    serializer_class: Type[QuoteSerializer] = QuoteSerializer


class QuoteDetail(RetrieveUpdateDestroyAPIView):
    """Responsible for retrieving a single quote from an application.

    Endpoint is `/api/<id>`

    ``GET``: retrieve a single quote

    ``PUT``: updates a single quote

    ``DELETE``: deletes a single quote
    """

    permission_classes = (IsOwnerOrReadOnly,)
    queryset: List[Quote] = Quote.objects.all()
    serializer_class: Type[QuoteSerializer] = QuoteSerializer
