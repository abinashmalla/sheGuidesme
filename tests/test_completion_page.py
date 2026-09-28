import pytest
from pages.Login_page import HomePage
from pages.profile_page import ProfilePage
from pages.profile_completion_page import ProfileCompletionPage


@pytest.mark.parametrize(
    "browser",
    ["chrome"]
)

@pytest.mark.xfail
def test_complete_profile(driver, browser):

    login_page = HomePage(driver)
    profile_page = ProfilePage(driver)
    profile = ProfileCompletionPage(driver)

    login_page.open()

    login_page.login(email="abinashm498@gmail.com",password="Omabinash@100"
    )

    # Open Profile Completion

    profile_page.open_profile_completion()
    # Personal Information


    profile.enter_phone("+977 984 965 8392")

    profile.enter_social_media("9849658392")

    profile.enter_city("Kathmandu")

    profile.select_current_location()

    profile.enter_birth_date("1997-01-09")

    profile.click_next()

    # Profile Image

    profile.upload_profile_image("test_data/7b0f29c8-dd0f-4f50-88ee-b25408aa113b (1).jpg")

    profile.set_crop_zoom("1")

    profile.select_full_image()

    # Location

    profile.select_country("Nepal")

    profile.select_city("Kathmandu")

    # Personal Details

    profile.select_body_colour("Medium")

    profile.select_gender("female")

    profile.enter_religion("Hindu")

    profile.select_language("English")

    profile.click_next()

    # Professional Information

    profile.select_experience("3")

    profile.enter_profession("IT Engineer")

    profile.upload_training_certificate("test_data/0-31-1200x743.jpg")

    profile.upload_resume("test_data/ABINASH_MALLA_THAKURI_CV.pdf")

    # Service Charge

    profile.select_service_charge("20000","50000")

    profile.click_next()

    # Skills

    profile.select_skill("CCTV camera installation")

    profile.select_skill("Communication Dialogue and")

    profile.select_skill("Computer-Laptop repair service")

    # About Me

    profile.enter_about_me("Perfect for all")

    profile.enter_available_time("10:00","18:00")

    # Submit

    profile.submit()


    # Validation

    assert "profile" in driver.current_url.lower()