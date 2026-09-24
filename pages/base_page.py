from playwright.sync_api import Page, Locator

class BasePage:
    """Base class containing common page interactions and utility methods."""

    def __init__(self, page: Page):
        self.page = page

    def navigate_to(self, url: str) -> None:
        """Navigates to the specified URL."""
        self.page.goto(url)

    def get_element(self, selector: str) -> Locator:
        """Returns a locator for the given selector."""
        return self.page.locator(selector)
