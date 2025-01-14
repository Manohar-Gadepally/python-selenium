from selenium import webdriver
from selenium.webdriver.webkitgtk.webdriver import WebDriver


class DriverUtils:
    __driver = None

    @classmethod
    def get_driver(cls) -> WebDriver:
        if DriverUtils.__driver is None:
            options = webdriver.ChromeOptions()
            # options.add_argument("--headless")
            options.add_argument("start-maximized")
            DriverUtils.__driver = webdriver.Chrome(options=options)
        return DriverUtils.__driver
