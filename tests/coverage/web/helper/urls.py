from urequest.url import Address, HttpsUrl


class HomePageUrl(Address):
    """Home page url interface."""

    def __init__(self) -> None:
        self._home_url: Address = HttpsUrl(host="quote-quote.herokuapp.com")

    def matcher(self) -> str:
        return self._home_url.matcher()

    def host(self) -> str:
        return self._home_url.host()

    def __str__(self) -> str:
        return str(self._home_url)


class EditPageUrl(Address):
    """Home page url interface."""

    def __init__(self, page_id: int) -> None:
        self._edit_url: Address = HttpsUrl(
            host="quote-quote.herokuapp.com", path=f"edit/{page_id}"
        )

    def matcher(self) -> str:
        return self._edit_url.matcher()

    def host(self) -> str:
        return self._edit_url.host()

    def __str__(self) -> str:
        return str(self._edit_url)


class NewPageUrl(Address):
    """New quote page url interface."""

    def __init__(self) -> None:
        self._new_url: Address = HttpsUrl(
            host="quote-quote.herokuapp.com", path="new"
        )

    def matcher(self) -> str:
        return self._new_url.matcher()

    def host(self) -> str:
        return self._new_url.host()

    def __str__(self) -> str:
        return str(self._new_url)
