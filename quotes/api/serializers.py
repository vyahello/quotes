"""Contains API for serializers."""
from typing import Sequence, Type
from rest_framework.serializers import ModelSerializer
from app.models import Quote


class QuoteSerializer(ModelSerializer):
    """Represents quote serializer."""

    class Meta:
        """Represents meta configuration."""

        model: Type[Quote] = Quote
        fields: Sequence[str] = ("quote", "author", "source", "cover", "user")
