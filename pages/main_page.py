from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class MainPage:

    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)
        self.search_box = (By.XPATH, "(//input[@class='flex-1 px-4 py-2 text-[13px] lg:text-[16px] outline-none rounded-l-full cursor-pointer'])[1]")
        self.search_for_service = (By.XPATH,"(//input[@placeholder='Search for Service Provider & Travel Guide'])[1]")
        self.filter_by_town = (By.XPATH,"//input[@placeholder='Enter address...']")
        self.search_service_provider = (By.XPATH,"//button[@class='w-full sm:w-auto px-6 py-2.5 lg:py-2 bg-rose-500 text-white rounded-full hover:bg-rose-600 transition text-sm disabled:opacity-50 disabled:cursor-not-allowed']")
        self.chat=(By.XPATH,"//button[normalize-space()='Chat']")
        self.chat_box = (By.XPATH,"//input[@placeholder='Type a message...']")
        self.send = (By.XPATH,"//span[@class='hidden sm:inline ml-1']")
        self.home = (By.XPATH,"//a[normalize-space()='Home']")
        self.button = (By.XPATH,"(//button[@class='flex items-center gap-1 transition-colors hover:text-red-500'])[1]")
        self.like = (By.XPATH,"(//*[name()='path'])[11]")
        self.comment = (By.XPATH,"(//*[name()='svg'][@stroke='currentColor'])[5]")
        self.input_comment = (By.XPATH,"//textarea[@placeholder='Write a comment...']")
        self.search_div = (By.XPATH,"(//div[@class='relative mt-3'])[1]")
        self.search = (By.XPATH, "//input[@placeholder='Search']")


    def like_and_comment_post(self, comment_text: str = "perfect") -> None:
        self.driver.execute_script("window.scrollTo(0, 350)")
        time.sleep(3)
        self.wait.until(EC.visibility_of_element_located(self.button))
        time.sleep(2)
        self.wait.until(EC.element_to_be_clickable(self.like)).click()
        time.sleep(3)
        self.wait.until(EC.element_to_be_clickable(self.comment)).click()
        time.sleep(2)
        comment_input = self.wait.until(EC.visibility_of_element_located(self.input_comment))
        time.sleep(2)
        comment_input.clear()
        comment_input.send_keys(comment_text)
        time.sleep(3)


    def open_search(self):
        time.sleep(6)
        self.wait.until(EC.presence_of_element_located(self.search_box,)).click()
        time.sleep(3)
        sea = self.wait.until(EC.presence_of_element_located(self.search_for_service))
        sea.send_keys("Abinash Malla")
        time.sleep(2)
        sea.click()
        place = self.wait.until(EC.presence_of_element_located(self.filter_by_town))
        place.send_keys("Anamnagar")
        time.sleep(2)
        search_button = self.wait.until(EC.presence_of_element_located(self.search_service_provider))
        search_button.click()
        time.sleep(3)

    def open_chat(self):
        self.wait.until(EC.presence_of_element_located(self.chat)).click()
        time.sleep(3)
        chat_box = self.wait.until(EC.presence_of_element_located(self.chat_box))
        chat_box.send_keys("Hey")
        self.wait.until(EC.presence_of_element_located(self.send)).click()
        time.sleep(3)


    def open_home(self):
        self.wait.until(EC.presence_of_element_located(self.home)).click()
        time.sleep(3)

    def search(self):
        self.wait.until(EC.presence_of_element_located(self.search_div))
        box = self.wait.until(EC.presence_of_element_located(self.search))
        box.clear()
        time.sleep(2)
        box.send_keys("Abinash Malla")
        box.send_keys(Keys.RETURN)
        time.sleep(3)