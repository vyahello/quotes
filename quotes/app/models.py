"""Module represents API for database models."""
from typing import List
from django.db.models import CharField, DateTimeField, Field, Model, TextField, URLField


class Quote(Model):
    """Represents quote database model."""

    quote: Field = TextField()
    author: Field = CharField(max_length=100)
    source: Field = URLField(blank=True, null=True)
    cover: Field = URLField(blank=True, null=True)
    added: Field = DateTimeField(auto_now_add=True)
    edited: Field = DateTimeField(auto_now=True)

    def __str__(self) -> str:
        """Returns quote as a string."""
        return f"{self.quote} - {self.author}"

    class Meta:
        """Represents quote meta data."""

        ordering: List[str] = ["-added"]
