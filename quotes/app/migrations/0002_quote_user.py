"""Contains interfaces for initial migrations."""
from typing import Any, List
from django.conf import settings
from django.db.migrations import AddField, Migration as BaseMigration, swappable_dependency
from django.db.models import ForeignKey
from django.db.models.deletion import CASCADE


class Migration(BaseMigration):
    """Represents quote user migration."""

    dependencies: List[Any] = [
        swappable_dependency(settings.AUTH_USER_MODEL),
        ("app", "0001_initial"),
    ]
    operations: List[AddField] = [
        AddField(
            model_name="quote",
            name="user",
            field=ForeignKey(blank=True, null=True, on_delete=CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
