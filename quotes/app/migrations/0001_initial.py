"""Contains interfaces for initial migrations."""
from typing import List
from django.db import migrations, models


class Migration(migrations.Migration):
    """Represents internal migration."""

    initial: bool = True
    dependencies: List[str] = []
    operations: List[migrations.CreateModel] = [
        migrations.CreateModel(
            name="Quote",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("quote", models.TextField()),
                ("author", models.CharField(max_length=100)),
                ("source", models.URLField(blank=True, null=True)),
                ("cover", models.URLField(blank=True, null=True)),
                ("added", models.DateTimeField(auto_now_add=True)),
                ("edited", models.DateTimeField(auto_now=True)),
            ],
            options={"ordering": ["-added"]},
        ),
    ]
