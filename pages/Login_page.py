from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class HomePage:
    URL = "https://admin:admin@sheguidesme.com/"

    # Store locators as tuples (By, "selector")
    INITIAL_LOGIN_BTN = (By.XPATH, "//button[contains(@class, 'hover:bg-rose-50')]")
    EMAIL_INPUT = (By.XPATH, "//input[@placeholder='Email or Phone Number']")
    PASSWORD_INPUT = (By.ID, "password")
    SUBMIT_LOGIN_BTN = (By.XPATH, "//button[@type='submit'][normalize-space()='Login']")
    home = (By.LINK_TEXT, "Home")

    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def open(self):
        self.driver.get(self.URL)

    def click_initial_login(self):
        btn = self.wait.until(EC.element_to_be_clickable(self.INITIAL_LOGIN_BTN))
        time.sleep(3)
        btn.click()

    def enter_email(self, email):
        field = self.wait.until(EC.visibility_of_element_located(self.EMAIL_INPUT))
        field.clear()
        time.sleep(3)
        field.send_keys(email)

    def enter_password(self, password):
        field = self.wait.until(EC.visibility_of_element_located(self.PASSWORD_INPUT))
        field.clear()
        time.sleep(3)
        field.send_keys(password)

    def click_submit_login(self):
        btn = self.wait.until(EC.element_to_be_clickable(self.SUBMIT_LOGIN_BTN))
        time.sleep(3)
        btn.click()

    def login(self, email, password):
        self.click_initial_login()
        self.enter_email(email)
        self.enter_password(password)
        self.click_submit_login()
        time.sleep(4)





