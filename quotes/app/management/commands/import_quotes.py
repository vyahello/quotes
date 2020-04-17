"""Module contains import quotes `manage.py` command."""
# flake8: noqa
import sys
from csv import DictReader
from typing import Any, List
from django.contrib.auth.models import User
from django.core.management.base import BaseCommand, CommandParser
import requests
from app.models import Quote  # pylint: disable=import-error


class Command(BaseCommand):
    """Represents import quotes command."""

    QUOTES_URL: str = "https://raw.githubusercontent.com/bbelderbos/inspirational-quotes/master/Quotes.csv"
    DEFAULT_LIMIT: str = 20

    help: str = "Script to insert a set of quotes in our demo app"

    def add_arguments(self, parser: CommandParser) -> None:
        """Adds arguments to the command."""
        parser.add_argument(
            "--username", dest="username", default="quoteuser", help="username to associate the quotes with",
        )
        parser.add_argument(
            "--limit",
            dest="limit",
            default=self.DEFAULT_LIMIT,
            help=f"number of quotes to create (default = {self.DEFAULT_LIMIT})",
        )

    def handle(self, *args: Any, **options: Any) -> None:
        """Handles records creation."""
        if Quote.objects.count() > 0:
            sys.exit("Not an empty DB, cowardly exiting")

        username: str = options["username"]
        try:
            user: User = User.objects.get(username=username)
        except User.DoesNotExist:  # pylint: disable=no-member
            error: str = (
                f"User {username} does not exist in DB, create it " "via manage.py or register on the quotes site"
            )
            sys.exit(error)

        try:
            max_quotes: int = int(options["limit"])
        except ValueError:
            sys.exit("Please specify an numeric value for limit")

        headers: List[str] = "quote author genre".split()
        reader = DictReader(requests.get(self.QUOTES_URL).text.strip().splitlines(), fieldnames=headers, delimiter=";")

        quotes: List[Quote] = []
        for row in list(reader)[1 : max_quotes + 1]:
            quotes.append(Quote(quote=row["quote"], author=row["author"], user=user))

        Quote.objects.bulk_create(quotes)
        print(f"Done: {max_quotes} quotes created")
