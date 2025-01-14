import pytest
from main.utils.driver_utils import DriverUtils


@pytest.fixture(scope="class")
def setup(request):
    driver = DriverUtils.get_driver()
    driver.maximize_window()
    driver.implicitly_wait(2000)
    request.cls.driver = driver
    yield
    driver.quit()
