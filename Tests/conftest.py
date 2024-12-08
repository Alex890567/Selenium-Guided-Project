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
