from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import subprocess
from time import time, sleep
import requests
import pytest
import os


root_dir = os.path.join(__file__, os.path.dirname(__file__))


def pytest_addoption(parser):
    parser.addoption("--url", default="http://myapp:8080")


@pytest.fixture(scope='session')
def config(request):
    url = request.config.getoption("--url")
    return { 'url': url }


# def pytest_configure():
#     timeout = 60
#     start_time = time()
#     subprocess.Popen(["sudo", "docker-compose", "up"])
#     while time() - start_time < timeout:
#         try:
#             requests.get(url="http://0.0.0.0:8080/")
#             break
#         except:
#             pass
#     else:
#         print(f'Application did not start for {timeout} sec')


# def pytest_unconfigure():
#     subprocess.Popen(["sudo", "docker-compose", "down"])


@pytest.fixture(scope='function')
def driver(config):
    os.environ['WDM_LOG_LEVEL'] = '0'
    manager = ChromeDriverManager(version='latest')
    driver = webdriver.Chrome(executable_path=manager.install())
    # service = Service(executable_path='code/chromedriver')
    # driver = webdriver.Chrome(executable_path='code/chromedriver')
    driver.get(config['url'])
    yield driver
    driver.quit()
