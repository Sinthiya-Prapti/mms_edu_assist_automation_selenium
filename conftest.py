import pytest
from utils.driver_factory import get_driver
@pytest.fixture
def setup():
    driver = get_driver()
    yield driver
    driver.quit()

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call" and rep.failed:
        driver = item.funcargs['setup']
        driver.save_screenshot("failure.png")