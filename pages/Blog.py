from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class BlogPage:


    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)
        self.blog = (By.LINK_TEXT, "Blog")
        self.read_more = (By.XPATH, "//article[2]//a[1]//div[2]//button[1]")



    def click_blog(self):
        blog = self.wait.until(EC.element_to_be_clickable(self.blog))

        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});",
            blog
        )

        blog.click()

        self.wait.until(EC.element_to_be_clickable(self.read_more))

        return self.driver.current_url