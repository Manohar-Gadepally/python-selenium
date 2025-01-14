from selenium.webdriver.support.wait import WebDriverWait

from main.common.enums.products import Product
from selenium.webdriver.webkitgtk.webdriver import WebDriver


class Base:

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def launch_application(self, product: Product):
        self.driver.get(product.value)
        self.wait_for_page_load()

    def wait_for_page_load(self):
        WebDriverWait(self.driver, 5).until(
            lambda driver: driver.execute_script('return document.readyState;') == "complete")
