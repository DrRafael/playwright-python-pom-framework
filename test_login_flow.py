import pytest
from pages.login_page import LoginPage

def test_successful_login(login_page: LoginPage):
    """Verify end-to-end successful login workflow using Page Object Model."""
    login_page.load()
    login_page.login("tomsmith", "SuperSecretPassword!")
    login_page.verify_success_message("You logged into a secure area!")