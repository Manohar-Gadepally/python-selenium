import allure
import pytest

from main.products.online_shop.components.navbar_component import NavBarComponent
from main.products.online_shop.pages.login_page import Login


@pytest.mark.usefixtures("setup")
class TestOnlineShopBase:

    @pytest.fixture(autouse=True)
    def before(self):
        login_page = Login(self.driver)
        login_page.login_to_application("standard_user", "secret_sauce")

    @pytest.mark.smoke
    @pytest.mark.sanity
    @allure.title("Test Login")
    @allure.description("Tests if logged in or not")
    def test_login(self):
        nav_bar_component = NavBarComponent(self.driver)
        assert nav_bar_component.is_navbar_displayed()

    @pytest.mark.sanity
    @allure.title("Test logo")
    @allure.description("Tests if log has correct text")
    def test_logo(self):
        nav_bar_component = NavBarComponent(self.driver)
        assert nav_bar_component.get_logo() == "Swag Labs"

    @pytest.mark.sanity
    @allure.title("Test landing page title")
    @allure.description("Tests title of landing page")
    def test_landing_page_title(self):
        nav_bar_component = NavBarComponent(self.driver)
        assert nav_bar_component.get_page_title() == "Products"

    @allure.title("Test cart page title")
    @allure.description("Tests cart page title")
    def test_cart_page_title(self):
        nav_bar_component = NavBarComponent(self.driver)
        nav_bar_component.click_on_cart()
        assert nav_bar_component.get_page_title() == "Your Cart"
