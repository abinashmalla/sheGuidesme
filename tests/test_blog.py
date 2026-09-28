import time
from pages.Blog import BlogPage
from pages.Login_page import HomePage
from pages.profile_page import ProfilePage


def test_open_blog_page(driver):
    home_page = HomePage(driver)
    # Navigate to application
    home_page.open()

    # Execute login sequence
    home_page.login("abinashm498@gmail.com", "Omabinash@100")
    time.sleep(3)
    profile_page = ProfilePage(driver)
    profile_page.test_profile()
    time.sleep(3)
    x = 0
    while True:
        x += 1
        driver.execute_script("scrollBy(0,50)")
        time.sleep(0.10)
        if x > 100:
            break
    time.sleep(3)
    blog_page = BlogPage(driver)
    blog_page.click_blog()
    time.sleep(5)
    x = 0
    while True:
        x += 1
        driver.execute_script("scrollBy(0,50)")
        time.sleep(0.10)
        if x > 100:
            break