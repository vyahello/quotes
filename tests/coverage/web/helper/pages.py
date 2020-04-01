from abc import ABC, abstractmethod
from selenium.webdriver.remote.webdriver import WebDriver
from urequest.url import Address, HttpsUrl


class Page(ABC):
    """Base page interface."""

    @abstractmethod
    def navigate(self) -> None:
        pass

    @abstractmethod
    def loaded(self) -> bool:
        pass


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
        self._page: Page = QuotesPage(browser, HttpsUrl("quote-quote.herokuapp.com"))

    def navigate(self) -> None:
        self._page.navigate()

    def loaded(self) -> bool:
        return self._page.loaded()

    def title(self) -> str:
        return self._browser.find_element_by_id("pageTitle").text

    def add_quote_button_displayed(self) -> bool:
        return self._browser.find_element_by_id("new").is_displayed()

    def about_button_displayed(self) -> None:
        return self._browser.find_element_by_id("about").is_displayed()

    def login_button_displayed(self) -> None:
        return self._browser.find_element_by_id("login").is_displayed()
