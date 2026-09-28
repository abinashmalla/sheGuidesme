import time
from pages.Login_page import HomePage
from pages.main_page import MainPage
import pytest
from utils.driver_factory import get_driver

@pytest.fixture(params=["chrome", "firefox", "ChromiumEdge"])
def test_login_success(driver, request):
    browser = request.param
    driver = get_driver(browser)
    home_page = HomePage(driver)
    home_page.open()
    home_page.login("abinashm498@gmail.com","Omabinash@100")
    time.sleep(5)


def test_home_page(driver,test_login_success):
    home_page = HomePage(driver)
    home_page.open()
    home_page.login("abinashm498@gmail.com","Omabinash@100")
    time.sleep(3)
    main_page = MainPage(driver)
    time.sleep(3)
    main_page.open_search()
    time.sleep(3)

    # Scroll page
    for _ in range(100):
        driver.execute_script("window.scrollBy(0, 50);")
        time.sleep(0.10)
    # Return home
    main_page.open_home()
    time.sleep(4)