import profile

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class ProfilePage:
    URL = "https://admin:admin@sheguidesme.com/"
    profile_logo = (By.XPATH, "//div[@class='hidden md:flex items-center gap-6']//img[@alt='Profile']")
    my_profile = (By.XPATH, "//span[@class='flex items-center gap-3']")
    profile_image = (By.XPATH, "//a[@class='flex items-center justify-center space-x-4']//img[@alt='profile']")

    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def test_profile(self):
        logo = self.wait.until(EC.visibility_of_element_located(self.profile_logo))
        time.sleep(2)
        logo.click()
        pro = self.wait.until(EC.visibility_of_element_located(self.my_profile))
        time.sleep(2)
        pro.click()
        time.sleep(2)
        pro_img = self.wait.until(EC.visibility_of_element_located(self.profile_image))
        pro_img.click()
        time.sleep(3)