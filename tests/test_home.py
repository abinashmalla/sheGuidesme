import time
import pytest
from pages.Login_page import HomePage
from pages.main_page import MainPage

@pytest.fixture
def test_login_success(driver):
    home_page = HomePage(driver)
    # Navigate to application
    home_page.open()
    home_page.login("abinashm498@gmail.com", "Omabinash@100")
    time.sleep(5)


def test_home_page(driver, test_login_success):
    main_page = MainPage(driver)
    main_page.open_search()
    time.sleep(3)
    x = 0
    while True:
        x += 1
        driver.execute_script("scrollBy(0,50)")
        time.sleep(0.10)
        if x > 100:
            break
    main_page.open_home()
    time.sleep(3)
    # driver.switch_to.default_content()
    # main_page.search()
    # time.sleep(3)






