import pytest
from ui.capability import capability_select
from appium import webdriver


def pytest_addoption(parser):
    parser.addoption('--appium', default='http://127.0.0.1:4723/wd/hub')


@pytest.fixture(scope='session')
def config(request):
    appium = request.config.getoption('--appium')
    return {'appium': appium}


@pytest.fixture(scope='function')
def driver(config):
    desired_caps = capability_select()
    driver = webdriver.Remote(config['appium'], desired_capabilities=desired_caps)
    yield driver
    driver.quit()




