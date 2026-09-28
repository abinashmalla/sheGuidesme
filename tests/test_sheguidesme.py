import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Page Element Locators
LOC_LOGIN_BTN = (By.XPATH, "//button[normalize-space()='Login']")
LOC_EMAIL_INPUT = (By.XPATH, "//input[@placeholder='Email or Phone Number']")
LOC_PASSWORD_INPUT = (By.ID, "password")
LOC_SUBMIT_LOGIN = (By.XPATH, "//button[@type='submit' and normalize-space()='Login']")
LOC_LIKE_BTN = (By.XPATH, "//button[.//span[normalize-space()='0']][1]")
LOC_COMMENT_ICON = (By.XPATH, "(//*[name()='svg'][@stroke='currentColor'])[7]")
LOC_COMMENT_TEXTAREA = (By.XPATH, "//textarea[@placeholder='Write a comment...']")


def perform_login(driver, wait, config):
    #Helper action to handle authentication steps.
    driver.get(config["base_url"])

    login_button = wait.until(EC.element_to_be_clickable(LOC_LOGIN_BTN))
    login_button.click()

    email_input = wait.until(EC.visibility_of_element_located(LOC_EMAIL_INPUT))
    email_input.clear()
    email_input.send_keys(config["email"])

    password_input = wait.until(EC.visibility_of_element_located(LOC_PASSWORD_INPUT))
    password_input.clear()
    password_input.send_keys(config["password"])

    submit_login = wait.until(EC.element_to_be_clickable(LOC_SUBMIT_LOGIN))
    submit_login.click()

    # Condition assertion: Redirected to profile page
    wait.until(lambda d: "/profile" in d.current_url)

@pytest.mark.xfail
def test_login_and_social_interactions(driver, config):
    #Validates login, post like, and comment posting functionality.
    wait = WebDriverWait(driver, 20)

    # 1. Action: Perform Login
    perform_login(driver, wait, config)
    assert "/profile" in driver.current_url, "User failed to land on profile page post-login."

    # 2. Action: Navigate to Home Feed
    driver.get(config["base_url"])
    wait.until(lambda d: d.execute_script("return document.readyState") == "complete")

    # Scroll to trigger feed rendering
    driver.execute_script("window.scrollTo(0, 350);")

    # 3. Action: Like a post
    like_button = wait.until(EC.element_to_be_clickable(LOC_LIKE_BTN))
    driver.execute_script("arguments[0].scrollIntoView({block:'center'});", like_button)
    like_button.click()

    # 4. Action: Open comment box
    comment_btn = wait.until(EC.element_to_be_clickable(LOC_COMMENT_ICON))
    driver.execute_script("arguments[0].scrollIntoView({block:'center'});", comment_btn)
    comment_btn.click()

    # 5. Action: Post comment
    comment_text = "perfect"
    comment_input = wait.until(EC.visibility_of_element_located(LOC_COMMENT_TEXTAREA))
    driver.execute_script("arguments[0].scrollIntoView({block:'center'});", comment_input)
    comment_input.click()
    comment_input.clear()
    comment_input.send_keys(comment_text)
    comment_input.send_keys(Keys.RETURN)

    # 6. Condition Assertion: Verify comment appears in DOM
    posted_comment = wait.until(
        EC.presence_of_element_located(
            (By.XPATH, f"//*[normalize-space()='{comment_text}']")
        )
    )
    assert posted_comment.is_displayed(), f"Comment '{comment_text}' was not rendered on screen."