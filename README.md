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
