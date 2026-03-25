import json
import os
from zipfile import error

import pytest
from pages.login_page import LoginPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#
# def test_login_valid(setup):
#     driver = setup
#     driver.get("https://test-agency-mmsglobal.doer.school/login")
#     # json file read
#     with open("data_login.json") as f:
#         data = json.load(f)
#
#     login = LoginPage(driver)
#     login.login(data["username"], data["password"])
#     assert "Agency Admin" in driver.title

# ...................................................................

# def test_login_invalid(setup):
#     driver = setup
#     driver.get("https://test-agency-mmsglobal.doer.school/login")
#
#     login = LoginPage(driver)
#     login.login("wronguser@gmail.com", "wrongpass")
#
#     # Wait for error span to appear
#     error_msg = WebDriverWait(driver, 20).until(
#         EC.visibility_of_element_located(
#             (By.XPATH, "//span[contains(text(),'Something went wrong')]")
#         )
#     ).text
#
#     # Assertion
#     assert "Something went wrong" in error_msg

# Load test data
with open("data_login.json") as f:
    login_data = json.load(f)

@pytest.mark.parametrize("data", login_data)
def test_login_data_driven(setup, data):
    driver = setup
    driver.get("https://test-agency-mmsglobal.doer.school/login")
    login = LoginPage(driver)
    login.login(data["username"], data["password"])

    if data["type"] == "valid":
        # wait for dashboard page
        WebDriverWait(driver, 10).until(
            EC.title_contains("Agency Admin")
        )
        assert "Agency Admin" in driver.title
    else:
        # wait for error span
        error_msg = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(
                (By.XPATH, "//span[contains(text(), 'Something went wrong')]")

            )
        ) .text
        assert "Something went wrong" in error_msg