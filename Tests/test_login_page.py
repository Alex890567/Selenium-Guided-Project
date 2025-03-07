import time
import pytest
from selenium.webdriver.common.by import By


class TestPositiveLogin:

    @pytest.mark.login
    @pytest.mark.positive
    def test_positive_login(self, driver):

        # Navigate to web page
        driver.get("https://practicetestautomation.com/practice-test-login/")
        time.sleep(3)

        # Type username student into Username field
        username_locator = driver.find_element(By.ID, "username")
        username_locator.send_keys("student")

        # Type password Password123 into Password field
        password_locator = driver.find_element(By.ID, "password")
        password_locator.send_keys("Password123")

        # Push Submit button
        submit_button_locator = driver.find_element(By.ID, "submit")
        submit_button_locator.click()
        time.sleep(2)

        # Verify new page URL contains practicetestautomation.com/logged-in-successfully/
        actual_url = driver.current_url
        assert actual_url == "https://practicetestautomation.com/logged-in-successfully/"

        # Verify new page contains expected text ('Logged In Successfully')
        text_locator = driver.find_element(By.TAG_NAME, "h1")
        actual_text = text_locator.text
        assert actual_text == "Logged In Successfully"

        # Verify button Log out is displayed on the new page
        log_out_button_locator = driver.find_element(By.LINK_TEXT, "Log out")
        assert log_out_button_locator.is_displayed()
