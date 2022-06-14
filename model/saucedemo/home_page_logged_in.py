from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException

HEADER_TITLE_LOC = (By.CSS_SELECTOR, '#header_container .title')
BURGER_MENU_BUTTON_LOC = (By.ID, 'react-burger-menu-btn')
LOGOUT_BUTTON_LOC = (By.ID, 'logout_sidebar_link')


class HomePageLoggedIn:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 4)

    # Actions
    def click_burger_menu_button(self):
        self.wait.until(EC.element_to_be_clickable(BURGER_MENU_BUTTON_LOC)).click()

    # Services
    def get_header_title_text(self):
        try:
            title_el = self.driver.find_element(HEADER_TITLE_LOC[0], HEADER_TITLE_LOC[1])
            return title_el.text if title_el.is_displayed() else ''
        except NoSuchElementException:
            return ''

    def get_logout_button_text(self):
        return self.wait.until(EC.visibility_of_element_located(LOGOUT_BUTTON_LOC)).text

    def logout(self):
        self.click_burger_menu_button()
        self.wait.until(EC.visibility_of_element_located(LOGOUT_BUTTON_LOC)).click()
