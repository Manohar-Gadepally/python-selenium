import allure

from main.common.pages.base_page import Base
from main.common.enums.products import Product
from selenium.webdriver.common.by import By


class Login(Base):
    USERNAME = (By.ID, "user-name")
    PASSWORD = (By.ID, "password")
    LOGIN_BTN = (By.ID, "login-button")

    def __init__(self, driver):
        super().__init__(driver)

    def __enter_username(self, username):
        self.logger.info(f"Entering username '{username}'")
        self.driver.find_element(*Login.USERNAME).click()
        self.driver.find_element(*Login.USERNAME).send_keys(username)
        return self

    def __enter_password(self, password):
        self.logger.info("Entering password")
        self.driver.find_element(*Login.PASSWORD).click()
        self.driver.find_element(*Login.PASSWORD).send_keys(password)
        return self

    def __click_on_login_button(self):
        self.logger.info("Clicking in login button")
        self.driver.find_element(*Login.LOGIN_BTN).click()
        self.wait_for_page_load()

    @allure.step("Logging into application")
    def login_to_application(self, username, password):
        self.launch_application(Product.ONLINE_SHOP)
        self.__enter_username(username)\
            .__enter_password(password)\
            .__click_on_login_button()
