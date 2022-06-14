from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException

BURGER_MENU_BUTTON_LOC = (By.ID, 'react-burger-menu-btn')
LOGOUT_BUTTON_LOC = (By.ID, 'logout_sidebar_link')


class HomePageLoggedIn():
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 4)

    def is_burger_icon_present(self):
        try:
            return self.driver.find_element(BURGER_MENU_BUTTON_LOC[0], BURGER_MENU_BUTTON_LOC[1]).is_displayed()
        except NoSuchElementException:
            return False

    def click_burger_menu_button(self):
        self.wait.until(EC.visibility_of_element_located(BURGER_MENU_BUTTON_LOC)).click()

    def get_logout_button_text(self):
        return self.wait.until(EC.visibility_of_element_located(LOGOUT_BUTTON_LOC)).text

    def logout(self):
        self.click_burger_menu_button()
        self.wait.until(EC.visibility_of_element_located(LOGOUT_BUTTON_LOC)).click()
