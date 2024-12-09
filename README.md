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

















