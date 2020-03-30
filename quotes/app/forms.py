"""Contains interfaces to form quotes."""
from typing import List, Type, Tuple
from django.forms import ModelForm
from .models import Quote


class QuoteForm(ModelForm):
    """Represents a single quote form."""

    class Meta:
        """Represents meta info."""

        model: Type[Quote] = Quote
        exclude: Tuple[str, ...] = ()
        field: List[str] = ["quote", "author", "source", "cover"]
