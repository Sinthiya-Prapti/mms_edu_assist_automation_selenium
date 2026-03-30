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
                (By.XPATH, "//span[contains(text(),'Invalid username')]")
            )
        ).text

        assert "Invalid username or password" in error_msg


    # একটি full improved data-driven login test template বানাবো, যা valid এবং invalid login দুইটাই handle করবে, এবং error message বা success message capture করবে।

    # import pytest
    # from selenium.webdriver.common.by import By
    # from selenium.webdriver.support.ui import WebDriverWait
    # from selenium.webdriver.support import expected_conditions as EC
    # from pages.login_page import LoginPage  # তোমার LoginPage class import
    #
    # # Example data-driven login data
    # login_data = [
    #     {"username": "validuser@example.com", "password": "validpass", "type": "valid"},
    #     {"username": "wronguser1@example.com", "password": "wrongpass1", "type": "invalid"},
    #     {"username": "wronguser2@example.com", "password": "wrongpass2", "type": "invalid"},
    # ]
    #
    # @pytest.mark.parametrize("data", login_data)
    # def test_login_data_driven(setup, data):
    #     driver = setup
    #     driver.get("https://test-agency-mmsglobal.doer.school/login")
    #     login = LoginPage(driver)
    #
    #     # Perform login
    #     login.login(data["username"], data["password"])
    #
    #     if data["type"] == "valid":
    #         # Wait for dashboard page
    #         WebDriverWait(driver, 10).until(
    #             EC.title_contains("Agency Admin")
    #         )
    #         assert "Agency Admin" in driver.title
    #         print(f"[SUCCESS] Login passed for user: {data['username']}")
    #     else:
    #         # Wait for invalid login error message
    #         error_msg_element = WebDriverWait(driver, 10).until(
    #             EC.visibility_of_element_located(
    #                 (By.XPATH, "//span[contains(text(), 'Invalid username or password.')]")
    #             )
    #         )
    #         error_msg = error_msg_element.text
    #         assert error_msg == "Invalid username or password."
    #         print(f"[ERROR] Login failed as expected for user: {data['username']} with message: {error_msg}")