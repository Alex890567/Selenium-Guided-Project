# Selenium-Guided-Project

## Description
This repository provides a comprehensive guided tutorial on using Selenium with Python and Pytest for web automation. It includes detailed test scripts for various scenarios, including positive and negative login tests, handling exceptions, and basic math functions. Designed to serve both as an educational resource for beginners and as part of a CV presentation, this project demonstrates practical test automation skills.

## Features
- Positive Login Tests
- Negative Login Tests
- Exception Handling Tests
- Basic Math Function Tests
- Automated Tests with Selenium

## Table of Contents
1. [Description](#description)
2. [Features](#features)
3. [Test Files](#test-files)
    - [Conftest File](#conftest-file)
    - [Exception Handling Scenarios](#exception-handling-scenarios)
    - [Positive Login Scenarios](#positive-login-scenarios)
    - [Negative Login Scenarios](#negative-login-scenarios)
    - [Math Functions](#math-functions)
4. [Testing Markers Configuration](#testing-markers-configuration)
5. [Running the Tests](#running-the-tests)
    - [Prerequisites](#prerequisites)
    - [Execute the Tests](#execute-the-tests)
6. [License](#license)
7. [Contact Information](#contact-information)
8. [Happy Testing](#happy-testing)

## Test Files

### Conftest File
The `conftest.py` file contains a pytest fixture for setting up and tearing down the Selenium WebDriver for Microsoft Edge. This fixture ensures that tests can run smoothly by managing the WebDriver lifecycle.

```python
import pytest
from selenium import webdriver

@pytest.fixture()
def driver():
    print("Creating Edge Driver")
    my_driver = webdriver.Edge()
    # my_driver.implicitly_wait(10)
    yield my_driver
    print("\nClosing Edge Driver")
    my_driver.quit()
```

*Explanation*:

- **import pytest**: Imports the pytest module for creating and using fixtures.

- **from selenium import webdriver**: Imports the Selenium WebDriver module.

- **@pytest.fixture()**: Decorator to define a pytest fixture.

- **print("Creating Edge Driver")**: Outputs a message indicating the creation of the Edge WebDriver.

- **my_driver = webdriver.Edge()**: Initializes a new instance of the Edge WebDriver.

- **# my_driver.implicitly_wait(10)**: (Commented out) Sets an implicit wait to make the driver wait up to 10 seconds for elements to appear before throwing an error.

- **yield my_driver**: Provides the WebDriver instance to the test functions.

- **print("\nClosing Edge Driver")**: Outputs a message indicating the closing of the Edge WebDriver.

- **my_driver.quit()**: Closes the Edge WebDriver and frees up resources.

#### Summary
The `conftest.py` file contains a crucial fixture for setting up and tearing down the Selenium WebDriver for Microsoft Edge. By managing the WebDriver lifecycle, this fixture ensures that tests can run smoothly and resources are properly managed. It simplifies test setup and teardown, making the testing process more efficient and reliable.

### Exception Handling Scenarios
This file is responsible for testing various exceptions that might occur during web interactions using the `pytest` framework and `selenium` for automation. Each test case targets a specific exception, ensuring that the web application handles these scenarios gracefully.

- **File**: [test_exceptions.py](link)

#### Imports

```python
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
```

*Explanation*:

- **pytest**: The main testing framework used to write and run the test cases.

- **By**: A module from `selenium.webdriver.common` that provides various locators to find web elements.

- **expected_conditions**: A module from `selenium.webdriver.support` that provides a set of predefined conditions to wait for during testing.

- **WebDriverWait**: A module from `selenium.webdriver.support.wait` that is used to set up explicit waits for conditions to be met before proceeding with the next step.

#### Test Class: TestExceptions
The `TestExceptions` class contains multiple test methods, each designed to handle and verify a specific exception in the web application.

#### 1. test_no_such_element_exception
The `test_no_such_element_exception` function verifies that the `NoSuchElementException` is handled correctly. It navigates to the practice test page, clicks an "Add" button, and waits for the second row input field to be displayed.

```python
@pytest.mark.exceptions
@pytest.mark.no_such_element
def test_no_such_element_exception(self, driver):
    # Navigate to web page
    driver.get("https://practicetestautomation.com/practice-test-exceptions/")

    # Click Add button
    add_button_locator = driver.find_element(By.ID, "add_btn")
    add_button_locator.click()

    wait = WebDriverWait(driver, 10)
    row2_input_field_element = wait.until(expected_conditions.presence_of_element_located((By.XPATH, "//div[@id='row2']/input")))
    # Verify Row 2 input field is displayed
    assert row2_input_field_element.is_displayed(), "Row 2 input field should be displayed but it's not"
```

*Explanation*:

- **driver.get()**: Opens the specified URL in the web browser.

- **driver.find_element()**: Locates the "Add" button by its ID and clicks it.

- **WebDriverWait**: Waits up to 10 seconds for the second row input field to appear.

- **assert**: Verifies that the input field is displayed.

#### 2. test_element_not_interactable_exception
The `test_element_not_interactable_exception` function ensures the correct handling of `ElementNotInteractableException`. It navigates to the practice test page, clicks an "Add" button, types text into the second row input field, and verifies the confirmation message after saving.

```python
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
    row2_input_field_element = wait.until(expected_conditions.presence_of_element_located((By.XPATH, "//div[@id='row2']/input")))
    # Type text into the second input field
    row2_input_field_element.send_keys("Beef")

    # Push Save button
    save_button_locator = driver.find_element(By.XPATH, "(//button[@id='save_btn'])[2]")
    save_button_locator.click()

    # Verify text saved
    text_saved_locator = driver.find_element(By.ID, "confirmation")
    confirmation_text = text_saved_locator.text
    assert confirmation_text == "Row 2 was saved", "Confirmation text should appear but it's not"
```

*Explanation*:

- **driver.get()**: Opens the specified URL in the web browser.

- **driver.find_element()**: Locates the "Add" button by its ID and clicks it.

- **WebDriverWait**: Waits up to 10 seconds for the second row input field to appear.

- **send_keys()**: Types the text "Beef" into the input field.

- **driver.find_element()**: Locates the "Save" button by its XPath and clicks it.

- **assert**: Verifies that the confirmation text "Row 2 was saved" appears.

#### 3. test_invalid_element_state_exception
The `test_invalid_element_state_exception` function verifies the handling of `InvalidElementStateException`. It navigates to the practice test page, clicks the "Edit" button to clear an input field, types new text, and verifies the confirmation message after saving.

```python
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
```

*Explanation*:

- **driver.get()**: Opens the specified URL in the web browser.

- **driver.find_element()**: Locates the "Edit" button by its ID and clicks it.

- **WebDriverWait**: Waits up to 10 seconds for the first row input field to be clickable.

- **clear()**: Clears the existing text in the input field.

- **send_keys()**: Types the text "Souvlaki" into the input field.

- **driver.find_element()**: Locates the "Save" button by its ID and clicks it.

- **WebDriverWait**: Waits for the confirmation element to be visible.

- **assert**: Verifies that the confirmation text "Row 1 was saved" appears.

#### 4. test_stale_element_reference_exception
The `test_stale_element_reference_exception` function verifies the handling of `StaleElementReferenceException`. It navigates to the practice test page, locates the "instructions" text element, clicks the "Add" button to add a new row, and verifies that the "instructions" text element is no longer displayed.

```python
@pytest.mark.exceptions
@pytest.mark.stale_element_reference_exception
def test_stale_element_reference_exception(self, driver):
    # Open page
    driver.get("https://practicetestautomation.com/practice-test-exceptions/")

    # Find the instructions text element
    instructions_text_element_locator = driver.find_element(By.ID, "instructions")
    assert instructions_text_element_locator.text == "Push 'Add' button to add another row", "Instructions text element does not apply"

    # Push add button
    add_button_locator = driver.find_element(By.ID, "add_btn")
    add_button_locator.click()

    # Verify instruction text element is no longer displayed
    wait = WebDriverWait(driver, 10)
    assert wait.until(expected_conditions.invisibility_of_element_located((By.ID, "instructions"))), "Instruction text element should no longer be displayed"
```

*Explanation*:

- **driver.get()**: Opens the specified URL in the web browser.

- **driver.find_element()**: Locates the "instructions" text element by its ID and verifies its text.

- **driver.find_element()**: Locates the "Add" button by its ID and clicks it.

- **WebDriverWait**: Waits up to 10 seconds for the "instructions" text element to become invisible.

- **assert**: Verifies that the "instructions" text element is no longer displayed after clicking the "Add" button.

#### 5. test_timeout_exception
The `test_timeout_exception` function verifies the handling of `TimeoutException`. It navigates to the practice test page, clicks the "Add" button to add a new row, waits for the second input field to be displayed, and verifies its visibility.

```python
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
    assert wait.until(expected_conditions.visibility_of_element_located((By.XPATH, "(//input[@class='input-field'])[2]")))

    row2_input_field_locator = driver.find_element(By.XPATH, "//div[@id='row2']/input")
    assert row2_input_field_locator.is_displayed(), "Row 2 input field should be displayed"
```

*Explanation*:

- **driver.get()**: Opens the specified URL in the web browser.

- **driver.find_element()**: Locates the "Add" button by its ID and clicks it.

- **WebDriverWait**: Waits up to 10 seconds for the second input field to become visible.

- **assert**: Verifies that the second input field is displayed after clicking the "Add" button.

#### Summary
The `TestExceptions` class contains a series of tests designed to handle and verify different Selenium exceptions while interacting with a practice test page. Each test case focuses on a specific exception type, ensuring robust handling of various potential issues in web automation.

### Positive Login Scenarios
This file contains test cases to validate the positive login functionality of a web application using Selenium WebDriver and pytest. It verifies that a user can successfully log in with valid credentials and checks the presence of expected elements on the post-login page.

#### Class: TestPositiveLogin
The `TestPositiveLogin` class includes test methods to confirm the successful login process for a user with valid credentials. It performs various assertions to ensure the login process works as intended and that the necessary elements are present on the page after login.

#### 1. test_positive_login
The `test_positive_login` function verifies the positive login scenario. It navigates to the practice test login page, enters valid credentials, submits the form, and verifies that the user is redirected to the success page with the expected text and logout button.

```python
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
```

*Explanation*:

- **driver.get()**: Opens the specified URL in the web browser.

- **time.sleep()**: Pauses the execution for a few seconds to allow the page to load fully.

- **driver.find_element()**: Locates the username and password fields by their IDs and enters the credentials.

- **submit_button_locator.click()**: Clicks the submit button to log in.

- **driver.current_url**: Checks the current URL to ensure it matches the expected success page URL.

- **driver.find_element(By.TAG_NAME, "h1")**: Locates the header element containing the success message and verifies its text.

- **driver.find_element(By.LINK_TEXT, "Log out")**: Locates the logout button and verifies it is displayed.

#### Summary
The `TestPositiveLogin` class ensures that the login functionality of the web application works correctly with valid credentials. The test verifies the correct redirection to the success page and the presence of expected elements, ensuring the reliability of the login process.
