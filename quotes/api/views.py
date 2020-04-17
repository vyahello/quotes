"""Module represents API for routes."""
from typing import List, Type
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from app.models import Quote
from .serializers import QuoteSerializer
from .permissions import IsOwnerOrReadOnly


class Quotes(ListCreateAPIView):
    """Responsible for retrieving all quotes from an application.

    Endpoint is `/api/`
    """

    queryset: List[Quote] = Quote.objects.all()
    serializer_class: Type[QuoteSerializer] = QuoteSerializer


class QuoteDetail(RetrieveUpdateDestroyAPIView):
    """Responsible for retrieving a single quote from an application.

    Endpoint is `/api/<id>`
    """

    permission_classes = (IsOwnerOrReadOnly,)
    queryset: List[Quote] = Quote.objects.all()
    serializer_class: Type[QuoteSerializer] = QuoteSerializer
