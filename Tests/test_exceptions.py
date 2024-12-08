import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestExceptions:

    @pytest.mark.exceptions
    @pytest.mark.no_such_element
    def test_no_such_element_exception(self, driver):
        # Navigate to web page
        driver.get("https://practicetestautomation.com/practice-test-exceptions/")

        # Click Add button
        add_button_locator = driver.find_element(By.ID, "add_btn")
        add_button_locator.click()

        wait = WebDriverWait(driver, 10)
        row2_input_field_element = wait.until(expected_conditions.presence_of_element_located((By.XPATH, "//div["
                                                                                                         "@id='row2"
                                                                                                         "']/input")))
        # Verify Row 2 input field is displayed
        assert row2_input_field_element.is_displayed(), "Row 2 input field should be displayed but it's not"

    @pytest.mark.exceptions
    @pytest.mark.element_not_interactable_exception
    def test_element_not_interactable_exception(self, driver):
        # Navigate to web page
        driver.get("https://practicetestautomation.com/practice-test-exceptions/")

        # Click Add button
        add_button_locator = driver.find_element(By.ID, "add_btn")
        add_button_locator.click()

        # Wait for the second row to load
        wait = WebDriverWait(driver, 10)
        row2_input_field_element = wait.until(expected_conditions.presence_of_element_located((By.XPATH, "//div["
                                                                                                         "@id='row2"
                                                                                                         "']/input")))
        # Type text into the second input field
        row2_input_field_element.send_keys("Beef")

        # Push Save button 
        save_button_locator = driver.find_element(By.XPATH, "(//button[@id='save_btn'])[2]")
        save_button_locator.click()

        # Verify text saved
        text_saved_locator = driver.find_element(By.ID, "confirmation")
        confirmation_text = text_saved_locator.text
        assert confirmation_text == "Row 2 was saved", "Confirmation text should appear but it's not"

    @pytest.mark.exceptions
    @pytest.mark.invalid_element_state_exception
    def test_invalid_element_state_exception(self, driver):
        # Open page
        driver.get("https://practicetestautomation.com/practice-test-exceptions/")

        # Clear input field
        edit_button_locator = driver.find_element(By.ID, "edit_btn")
        edit_button_locator.click()
        row1_input_field_locator = driver.find_element(By.XPATH, "//input[@class='input-field']")
        wait = WebDriverWait(driver, 10)
        wait.until(expected_conditions.element_to_be_clickable(row1_input_field_locator))
        row1_input_field_locator.clear()

        # Type text into the input field
        row1_input_field_locator.send_keys("Souvlaki")

        # Verify text changed
        save_button_locator = driver.find_element(By.ID, "save_btn")
        save_button_locator.click()
        wait = WebDriverWait(driver, 10)
        confirmation_element = wait.until(expected_conditions.visibility_of_element_located((By.ID, "confirmation")))

        actual_confirmation_text = confirmation_element.text
        assert actual_confirmation_text == "Row 1 was saved", "Confirmation text does not apply"

    @pytest.mark.exceptions
    @pytest.mark.stale_element_reference_exception
    def test_stale_element_reference_exception(self, driver):
        # Open page
        driver.get("https://practicetestautomation.com/practice-test-exceptions/")

        # Find the instructions text element
        instructions_text_element_locator = driver.find_element(By.ID, "instructions")
        assert instructions_text_element_locator.text == "Push “Add” button to add another row", "Instructions text " \
                                                                                                 "element does not " \
                                                                                                 "apply"

        # Push add button
        add_button_locator = driver.find_element(By.ID, "add_btn")
        add_button_locator.click()

        # Verify instruction text element is no longer displayed
        wait = WebDriverWait(driver, 10)
        assert wait.until(expected_conditions.invisibility_of_element_located((By.ID, "instructions"))), "instruction " \
                                                                                                         "text " \
                                                                                                         "element " \
                                                                                                         "should no " \
                                                                                                         "longer " \
                                                                                                         "displayed"

    @pytest.mark.exceptions
    @pytest.mark.timeout_exception
    def test_timeout_exception(self, driver):
        # Open page
        driver.get("https://practicetestautomation.com/practice-test-exceptions/")

        # Click Add button
        add_button_locator = driver.find_element(By.ID, "add_btn")
        add_button_locator.click()

        # Wait for 3 seconds for the second input field to be displayed
        wait = WebDriverWait(driver, 10)
        assert wait.until(
            expected_conditions.visibility_of_element_located((By.XPATH, "(//input[@class='input-field'])[2]")))

        row2_input_field_locator = driver.find_element(By.XPATH, "//div[@id='row2']/input")
        assert row2_input_field_locator.is_displayed(), "Row 2 input field should be displayed"
