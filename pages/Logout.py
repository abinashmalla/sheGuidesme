from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class LogoutPage:
    URL = "https://sheguidesme.com/"
    profile_logo = (By.XPATH, "//div[@class='hidden md:flex items-center gap-6']//img[@alt='Profile']")
    my_profile = (By.XPATH, "//span[@class='flex items-center gap-3']")
    logout_btn = (By.XPATH, "(//button[normalize-space()='Logout'])[1]")

    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def test_Logout(self):
        logo = self.wait.until(EC.visibility_of_element_located(self.profile_logo))
        time.sleep(2)
        logo.click()
        pro = self.wait.until(EC.visibility_of_element_located(self.my_profile))
        time.sleep(2)
        pro.click()
        time.sleep(2)
        logout = self.wait.until(EC.visibility_of_element_located(self.logout_btn))
        logout.click()
        time.sleep(3)




