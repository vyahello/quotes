from abc import ABC, abstractmethod
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from urequest.url import Address, HttpsUrl


class Page(ABC):
    """Base page interface."""

    @abstractmethod
    def navigate(self) -> None:
        pass

    @abstractmethod
    def loaded(self) -> bool:
        pass


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
        self._edit_url: Address = HttpsUrl(host="quote-quote.herokuapp.com", path=f"edit/{page_id}")

    def matcher(self) -> str:
        return self._edit_url.matcher()

    def host(self) -> str:
        return self._edit_url.host()

    def __str__(self) -> str:
        return str(self._edit_url)


class NewPageUrl(Address):
    """New quote page url interface."""

    def __init__(self) -> None:
        self._new_url: Address = HttpsUrl(host="quote-quote.herokuapp.com", path="new")

    def matcher(self) -> str:
        return self._new_url.matcher()

    def host(self) -> str:
        return self._new_url.host()

    def __str__(self) -> str:
        return str(self._new_url)


class QuotesPage(Page):
    """Unified quotes page interface."""

    def __init__(self, browser: WebDriver, url: Address) -> None:
        self._browser = browser
        self._url = url

    def navigate(self) -> None:
        self._browser.get(str(self._url))

    def loaded(self) -> bool:
        return str(self._url) in self._browser.current_url


class HomePage(Page):
    """Home page interface."""

    def __init__(self, browser: WebDriver) -> None:
        self._browser = browser
        self._page: Page = QuotesPage(browser, HomePageUrl())

    def navigate(self) -> None:
        self._page.navigate()

    def loaded(self) -> bool:
        return self._page.loaded()

    def title(self) -> str:
        return self._browser.find_element_by_id("pageTitle").text.strip()

    def add_quote_button_displayed(self) -> bool:
        return self._browser.find_element_by_id("new").is_displayed()

    def about_button_displayed(self) -> None:
        return self._browser.find_element_by_id("about").is_displayed()

    def login_button_displayed(self) -> None:
        return self._browser.find_element_by_id("login").is_displayed()

    def message(self) -> str:
        return self._browser.find_element_by_id("messages").text.strip()


class _Form:
    """Form input interface."""

    def __init__(self, browser: WebDriver) -> None:
        self._browser = browser

    def fill_quote(self, quote: str) -> None:
        self._fill(quote, location_id="id_quote", clear=True)

    def fill_author(self, author: str) -> None:
        self._fill(author, location_id="id_author", clear=True)

    def fill_source(self, source: str) -> None:
        self._fill(source, location_id="id_source", clear=True)

    def fill_cover(self, source: str) -> None:
        self._fill(source, location_id="id_cover", clear=True)

    def _fill(self, value: str, location_id: str, clear: bool = False) -> None:
        field: WebElement = self._browser.find_element_by_id(location_id)
        if clear:
            field.clear()
        field.send_keys(value)


class EditPage(Page):
    """Edit page interface."""

    def __init__(self, browser: WebDriver, page_id: int) -> None:
        self._browser = browser
        self._page: Page = QuotesPage(browser, EditPageUrl(page_id))
        self._form: _Form = _Form(browser)

    def navigate(self) -> None:
        self._page.navigate()

    def loaded(self) -> bool:
        return self._page.loaded()

    def form(self) -> _Form:
        return self._form

    def edit(self) -> HomePage:
        self._browser.find_element_by_id("edit").click()
        return HomePage(self._browser)


class NewPage(Page):
    """New page interface."""

    def __init__(self, browser: WebDriver) -> None:
        self._browser = browser
        self._page: Page = QuotesPage(browser, NewPageUrl())
        self._form: _Form = _Form(browser)

    def navigate(self) -> None:
        self._page.navigate()

    def loaded(self) -> bool:
        return self._page.loaded()

    def form(self) -> _Form:
        return self._form

    def new(self) -> HomePage:
        self._browser.find_element_by_css_selector("[value='New']").click()
        return HomePage(self._browser)
