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
        self.driver.find_element(By.CSS_SELECTOR, '.shopping_cart_links')
        try:
            burger = self.driver.find_element(BURGER_MENU_BUTTON_LOC[0], BURGER_MENU_BUTTON_LOC[1])
            print(f'displayed: {burger.is_displayed()}')
            print(f'enabled: {burger.is_enabled()}')
            print(f'size: {burger.rect}')
            self.driver.find_element(BURGER_MENU_BUTTON_LOC[0], BURGER_MENU_BUTTON_LOC[1]).click()
            return self.driver.find_element(BURGER_MENU_BUTTON_LOC[0], BURGER_MENU_BUTTON_LOC[1]).is_displayed()
        except NoSuchElementException:
            return False

    def click_burger_menu_button(self):
        self.wait.until(EC.element_to_be_clickable(BURGER_MENU_BUTTON_LOC)).click()

    def get_logout_button_text(self):
        return self.wait.until(EC.visibility_of_element_located(LOGOUT_BUTTON_LOC)).text

    def logout(self):
        self.click_burger_menu_button()
        self.wait.until(EC.visibility_of_element_located(LOGOUT_BUTTON_LOC)).click()
