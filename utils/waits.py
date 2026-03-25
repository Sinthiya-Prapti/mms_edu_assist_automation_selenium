from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.waits import wait_for_element
def wait_for_element(driver, locator):
    wait = WebDriverWait(driver, 10)
    return wait.until(EC.visibility_of_element_located(locator))

def enter_username(self, user):
    wait_for_element(self.driver, self.username).send_keys(user)