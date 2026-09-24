from playwright.sync_api import Page, expect
from pages.base_page import BasePage

class LoginPage(BasePage):
    """Page Object representing the Login Page and its actions."""

    URL = "https://the-internet.herokuapp.com/login"

    # Selectors
    USERNAME_INPUT = "#username"
    PASSWORD_INPUT = "#password"
    SUBMIT_BUTTON = "button[type='submit']"
    FLASH_MESSAGE = "#flash"

    def __init__(self, page: Page):
        super().__init__(page)

    def load(self) -> None:
        """Loads the login page."""
        self.navigate_to(self.URL)

    def login(self, username: str, password: str) -> None:
        """Executes the login operation with provided credentials."""
        self.page.fill(self.USERNAME_INPUT, username)
        self.page.fill(self.PASSWORD_INPUT, password)
        self.page.click(self.SUBMIT_BUTTON)

    def verify_success_message(self, expected_text: str) -> None:
        """Asserts that the success flash message is visible and contains expected text."""
        message_locator = self.get_element(self.FLASH_MESSAGE)
        expect(message_locator).to_be_visible()
        expect(message_locator).to_contain_text(expected_text)
