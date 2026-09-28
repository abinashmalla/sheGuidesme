import pytest
from pages.Login_page import HomePage


def test_login_success(driver):
    home_page = HomePage(driver)

    # Navigate to application
    home_page.open()

    # Execute login sequence
    home_page.login("abinashm498@gmail.com", "Omabinash@100")

    # Verification assertion
    assert "sheguidesme.com" in driver.current_url
