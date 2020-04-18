"""Module represents API for database models."""
from typing import List
from django.db.models import CASCADE, CharField, DateTimeField, Field, ForeignKey, Model, TextField, URLField
from django_registration.forms import User


class Quote(Model):
    """Represents quote database model."""

    quote: Field = TextField()
    author: Field = CharField(max_length=100)
    source: Field = URLField(blank=True, null=True)
    cover: Field = URLField(blank=True, null=True)
    added: Field = DateTimeField(auto_now_add=True)
    edited: Field = DateTimeField(auto_now=True)
    user: Field = ForeignKey(User, on_delete=CASCADE, blank=True, null=True)

    def __str__(self) -> str:
        """Returns quote as a string."""
        return f"{self.quote} - {self.author} (submitted by {self.user})"

    class Meta:
        """Represents quote meta data."""

        ordering: List[str] = ["-added"]
