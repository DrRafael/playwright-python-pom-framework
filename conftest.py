import pytest
from playwright.sync_api import Page
from pages.login_page import LoginPage

@pytest.fixture
def login_page(page: Page) -> LoginPage:
    """Fixture to initialize and return the LoginPage object."""
    return LoginPage(page)
