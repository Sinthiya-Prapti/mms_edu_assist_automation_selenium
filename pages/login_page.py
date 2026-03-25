from selenium.webdriver.common.by import By
class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    username = (By.ID, "agency-admin-login_username")
    password = (By.ID, "agency-admin-login_password")
    login_btn = (By.CSS_SELECTOR, "button[type='submit']")
    def enter_username(self, user):
        self.driver.find_element(*self.username).send_keys(user)

    def enter_password(self, pwd):
        self.driver.find_element(*self.password).send_keys(pwd)

    def click_login(self):
        self.driver.find_element(*self.login_btn).click()

    def login(self, user, pwd):
        self.enter_username(user)
        self.enter_password(pwd)
        self.click_login()
