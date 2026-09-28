import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC


class ProfileCompletionPage:

    PHONE_INPUT = (By.XPATH,"//input[contains(@placeholder, '1 (702) 123-')]")

    SOCIAL_MEDIA_INPUT = (By.XPATH,"//input[@placeholder='Enter your phone/social media']")

    CITY_INPUT = (By.XPATH,"//input[@placeholder='Enter your exact city/village']")

    BIRTH_DATE = (By.NAME,"birth_date")

    NEXT_BUTTON = (By.XPATH,"//form[@id='profile-form']//button[normalize-space()='Next']")

    COUNTRY_INPUT = (By.ID,"react-select-2-input")

    CITY_SELECT_INPUT = (By.ID,"react-select-3-input")

    BODY_COLOUR = (By.NAME,"body_colour")

    GENDER = (By.NAME,"gender")

    RELIGION_INPUT = (By.XPATH,"//input[@placeholder='Optional']")

    LANGUAGES_BUTTON = (By.XPATH,"//button[contains(., 'Select up to 3 languages')]")

    SKILLS_BUTTON = (By.XPATH,"//button[contains(., 'Select up to 3 skills')]")

    SERVICE_MIN = (By.NAME,"service_charge_min")

    SERVICE_MAX = (By.NAME,"service_charge_max")

    ABOUT_ME = (By.NAME,"about_me")

    TIME_FROM = (By.NAME,"time_from")

    TIME_TO = (By.NAME,"time_to")

    SUBMIT_BUTTON = (By.XPATH,"//button[normalize-space()='Submit']")

    TRAINING_CERTIFICATE = (By.NAME,"training_certificate")

    RESUME = (By.NAME,"resume")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    # Generic helper methods
    def click(self, locator):
        element = self.wait.until(EC.element_to_be_clickable(locator))

        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});",
            element
        )

        element.click()

    def type_text(self, locator, value):
        element = self.wait.until(EC.visibility_of_element_located(locator))

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});",
            element
        )

        element.clear()
        element.send_keys(value)

    def select_by_value(self, locator, value):
        element = self.wait.until(EC.visibility_of_element_located(locator))

        Select(element).select_by_value(value)

    def upload_file(self, locator, file_path):
        element = self.wait.until(EC.presence_of_element_located(locator))

        absolute_path = os.path.abspath(file_path)

        if not os.path.exists(absolute_path):
            raise FileNotFoundError(
                f"File not found: {absolute_path}"
            )

        element.send_keys("absolute_path")

    def scroll_to_bottom(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")


    # Personal information

    def enter_phone(self, phone):
        self.type_text(self.PHONE_INPUT, phone)

    def enter_social_media(self, social_media):
        self.type_text(self.SOCIAL_MEDIA_INPUT,
            social_media
        )

    def enter_city(self, city):
        self.type_text(self.CITY_INPUT, city)

    def select_current_location(self):
        location_button = (By.XPATH,"//*[normalize-space()='Use my current location']")

        self.click(location_button)

    def enter_birth_date(self, birth_date):
        self.type_text(self.BIRTH_DATE,birth_date)

    def click_next(self):
        self.click(self.NEXT_BUTTON)

    # Profile image

    def upload_profile_image(self, file_path):
        choose_file = (
            By.XPATH,
            "//input[@type='file']"
        )

        self.upload_file(
            choose_file,
            file_path
        )

    def set_crop_zoom(self, value="1"):
        slider = (
            By.XPATH,
            "//input[@type='range']"
        )

        element = self.wait.until(
            EC.presence_of_element_located(slider)
        )

        element.send_keys(value)

    def select_full_image(self):
        self.click(
            (
                By.XPATH,
                "//button[normalize-space()='Full Image']"
            )
        )

        self.click(
            (
                By.XPATH,
                "//button[normalize-space()='Use Full Image']"
            )
        )

    # Country / City

    def select_country(self, country):
        self.click(self.COUNTRY_INPUT)

        self.type_text(
            self.COUNTRY_INPUT,
            country
        )

        option = (
            By.XPATH,
            f"//*[@role='option' and normalize-space()='{country}']"
        )

        self.click(option)

    def select_city(self, city):
        self.click(self.CITY_SELECT_INPUT)

        self.type_text(
            self.CITY_SELECT_INPUT,
            city
        )

        option = (
            By.XPATH,
            f"//*[@role='option' and normalize-space()='{city}']"
        )

        self.click(option)

    # Basic profile details

    def select_body_colour(self, value):
        self.select_by_value(
            self.BODY_COLOUR,
            value
        )

    def select_gender(self, value):
        self.select_by_value(
            self.GENDER,
            value
        )

    def enter_religion(self, religion):
        self.type_text(
            self.RELIGION_INPUT,
            religion
        )

    # Languages

    def select_language(self, language):
        self.click(self.LANGUAGES_BUTTON)

        language_locator = (
            By.XPATH,
            f"//label[contains(normalize-space(), '{language}')]"
        )

        self.click(language_locator)

    # Professional details

    def select_experience(self, value):
        experience = (
            By.XPATH,
            "//select"
        )

        self.select_by_value(
            experience,
            value
        )

    def enter_profession(self, profession):
        profession_input = (
            By.XPATH,
            "//input[@placeholder='e.g. Medical, Hotel']"
        )

        self.type_text(
            profession_input,
            profession
        )

    def upload_training_certificate(self, file_path):
        self.upload_file(
            self.TRAINING_CERTIFICATE,
            file_path
        )

    def upload_resume(self, file_path):
        self.upload_file(
            self.RESUME,
            file_path
        )

    def select_service_charge(
        self,
        minimum,
        maximum
    ):
        self.type_text(
            self.SERVICE_MIN,
            minimum
        )

        self.type_text(
            self.SERVICE_MAX,
            maximum
        )

    # Skills

    def select_skill(self, skill):
        self.click(self.SKILLS_BUTTON)

        skill_locator = (
            By.XPATH,
            f"//label[contains(normalize-space(), '{skill}')]"
        )

        self.click(skill_locator)

    # About / availability

    def enter_about_me(self, text):
        self.type_text(
            self.ABOUT_ME,
            text
        )

    def enter_available_time(
        self,
        start_time,
        end_time
    ):
        self.type_text(
            self.TIME_FROM,
            start_time
        )

        self.type_text(
            self.TIME_TO,
            end_time
        )

    # Submit

    def submit(self):
        self.click(self.SUBMIT_BUTTON)