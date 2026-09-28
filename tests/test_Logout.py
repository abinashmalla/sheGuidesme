import time

import pytest

from pages.Login_page import HomePage
from pages.Logout import LogoutPage


def test_logout(driver):
    home_page = HomePage(driver)

    # Navigate to application
    home_page.open()

    # Execute login sequence
    home_page.login("abinashm498@gmail.com", "Omabinash@100")

    # Verification assertion
    assert "sheguidesme.com" in driver.current_url

    # Navigate to application

    Logout = LogoutPage(driver)

    Logout.test_Logout()

    assert "https://admin:admin@sheguidesme.com/" in driver.current_url