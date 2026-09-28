import time
from pages.Login_page import HomePage
from pages.Logout import LogoutPage
from pages.main_page import MainPage
from pages.profile_page import  ProfilePage


def test_End_to_End_Testing(driver):
    home_page = HomePage(driver)

    # Navigate to application
    home_page.open()

    # Execute login sequence
    home_page.login("abinashm498@gmail.com", "Omabinash@100")

    time.sleep(3)
    main_page = MainPage(driver)

    main_page.open_search()

    time.sleep(3)
    x = 0
    while True:
        x += 1
        driver.execute_script("scrollBy(0,50)")
        time.sleep(0.10)
        if x > 100:
            break
    main_page.open_home()

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

    Logout = LogoutPage(driver)

    Logout.test_Logout()
    time.sleep(3)