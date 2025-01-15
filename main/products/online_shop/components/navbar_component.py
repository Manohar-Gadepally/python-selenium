from selenium.webdriver.common.by import By

from main.common.pages.base_page import Base


class NavBarComponent(Base):
    NAV_BAR = (By.ID, "header_container")
    APP_LOGO = (By.CLASS_NAME, "app_logo")
    PAGE_TITLE = (By.CLASS_NAME, "title")
    SHOPPING_CART = (By.CLASS_NAME, "shopping_cart_link")

    def __init__(self, driver):
        super().__init__(driver)

    def is_navbar_displayed(self):
        is_displayed = self.driver.find_element(*NavBarComponent.NAV_BAR).is_displayed()
        self.logger.info(f"Nav bar is displayed: '{is_displayed}'")
        return is_displayed

    def get_logo(self):
        logo_text = self.driver.find_element(*NavBarComponent.APP_LOGO).text.strip()
        self.logger.info(f"Logo text is '{logo_text}'")
        return logo_text

    def get_page_title(self):
        page_title = self.driver.find_element(*NavBarComponent.PAGE_TITLE).text.strip()
        self.logger.info(f"Page title is '{page_title}'")
        return page_title

    def click_on_cart(self):
        self.logger.info("Clicking on cart")
        self.driver.find_element(*NavBarComponent.SHOPPING_CART).click()
        self.wait_for_page_load()
