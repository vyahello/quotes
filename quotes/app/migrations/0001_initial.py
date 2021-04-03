"""Contains interfaces for initial migrations."""
from typing import List
from django.db.migrations import CreateModel, Migration as BaseMigration
from django.db.models import (
    AutoField,
    CharField,
    DateTimeField,
    TextField,
    URLField,
)


class Migration(BaseMigration):
    """Represents initial migration."""

    initial: bool = True
    dependencies: List[str] = []
    operations: List[CreateModel] = [
        CreateModel(
            name="Quote",
            fields=[
                (
                    "id",
                    AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("quote", TextField()),
                ("author", CharField(max_length=100)),
                ("source", URLField(blank=True, null=True)),
                ["cover", URLField(blank=True, null=True)],
                ("added", DateTimeField(auto_now_add=True)),
                ("edited", DateTimeField(auto_now=True)),
            ],
            options={"ordering": ["-added"]},
        ),
    ]
