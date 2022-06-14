from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

LOGIN_BUTTON_ID = 'login-button'
USER_NAME_ID = 'user-name'
PASSWORD_ID = 'password'
ERROR_MESSAGE_XPATH = '//*[@id="login_button_container"]//h3'


class HomePageLoggedOut:

    def __init__(self, driver):
        self.driver = driver

    def type_username(self, username):
        self.driver.find_element(By.ID, USER_NAME_ID).send_keys(username)

    def type_password(self, password):
        self.driver.find_element(By.ID, PASSWORD_ID).send_keys(password)

    def click_login_button(self):
        self.driver.find_element(By.ID, LOGIN_BUTTON_ID).click()

    def get_error_message(self):
        try:
            error_message_el = self.driver.find_element(By.XPATH, ERROR_MESSAGE_XPATH)
            if error_message_el.is_displayed():
                return error_message_el.text
            else:
                return ''
        except NoSuchElementException:
            return ''

    def login(self, username, password):
        self.type_username(username)
        self.type_password(password)
        self.click_login_button()
