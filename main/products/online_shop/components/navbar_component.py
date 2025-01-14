from selenium.webdriver.common.by import By

from common.pages.base_page import Base


class NavBarComponent(Base):
    NAV_BAR = (By.ID, "header_container")
    APP_LOGO = (By.CLASS_NAME, "app_logo")
    PAGE_TITLE = (By.CLASS_NAME, "title")
    SHOPPING_CART = (By.CLASS_NAME, "shopping_cart_link")

    def __init__(self, driver):
        super().__init__(driver)

    def is_navbar_displayed(self):
        return self.driver.find_element(*NavBarComponent.NAV_BAR).is_displayed()

    def get_logo(self):
        return self.driver.find_element(*NavBarComponent.APP_LOGO).text.strip()

    def get_page_title(self):
        return self.driver.find_element(*NavBarComponent.PAGE_TITLE).text.strip()

    def click_on_cart(self):
        self.driver.find_element(*NavBarComponent.SHOPPING_CART).click()
        self.wait_for_page_load()
