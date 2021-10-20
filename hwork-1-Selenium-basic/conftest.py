import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption("--url", default="https://target.my.com/")


@pytest.fixture
def config(request):
    url = request.config.getoption("--url")
    return { 'url': url }


@pytest.fixture(autouse=True)
def driver(config):
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(config['url'])
    yield driver
    driver.close()
