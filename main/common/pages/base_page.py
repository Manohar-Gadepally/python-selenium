from selenium.webdriver.support.wait import WebDriverWait

from main.common.enums.products import Product
from selenium.webdriver.webkitgtk.webdriver import WebDriver

from main.utils.logger_utils import Logger


class Base:

    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.logger = Logger.get_logger()

    def launch_application(self, product: Product):
        self.driver.get(product.value)
        self.wait_for_page_load()

    def wait_for_page_load(self):
        WebDriverWait(self.driver, 5).until(
            lambda driver: driver.execute_script('return document.readyState;') == "complete")
