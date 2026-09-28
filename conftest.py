import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

BASE_URL = "https://sheguidesme.com/"
EMAIL = os.getenv("SHEGUIDESME_EMAIL", "abinashm498@gmail.com")
PASSWORD = os.getenv("SHEGUIDESME_PASSWORD", "Omabinash@100")


@pytest.fixture(scope="session")
def config():
    #Provides configuration constants across tests.
    return {
        "base_url": BASE_URL,
        "email": EMAIL,
        "password": PASSWORD
    }


@pytest.fixture(scope="function")
def driver(request):
    #Initializes and quits the WebDriver instance per test run.
    options = Options()
    options.add_argument("--start-maximized")
    options.add_argument("--disable-notifications")

    driver_instance = webdriver.Chrome(options=options)
    driver_instance.implicitly_wait(5)

    yield driver_instance

    driver_instance.quit()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    #Automatically captures screenshots on test failure.
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        driver_instance = item.funcargs.get("driver")
        if driver_instance:
            file_name = f"failure_{item.name}.png"
            driver_instance.save_screenshot(file_name)