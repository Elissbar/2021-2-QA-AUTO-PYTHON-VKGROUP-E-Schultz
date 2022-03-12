from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from orm.client import MySQLClient
import pytest
import logging
import shutil
import allure
import os


def pytest_addoption(parser):
    parser.addoption("--url", default="myapp:8081")
    # parser.addoption("--url", default="https://www.google.com/")
    parser.addoption("--mock", default="vk_mock:5000")
    parser.addoption("--debug_log", action='store_true')
    parser.addoption("--mysql", default="mysql:3306")
    parser.addoption("--selenoid", action='store_true')


@pytest.fixture(scope='session')
def config(request):
    url = request.config.getoption("--url")
    mock = request.config.getoption("--mock")
    mysql = request.config.getoption("--mysql")
    debug_log = request.config.getoption("--debug_log")
    selenoid = "selenoid:4444/wd/hub" if request.config.getoption('--selenoid') else None
    return { 'url': url, 'mock': mock, 'mysql': mysql, 'debug_log': debug_log, "selenoid": selenoid }


def pytest_configure(config):
    mysql_client = MySQLClient(host='mysql:3306', db='TEST')
    mysql_client.connect()
    config.mysql_client = mysql_client
    test_dir = os.path.join('tmp', 'test')
    if not hasattr(config, 'workerinput'):
        if os.path.exists(test_dir):
            shutil.rmtree(test_dir)
        os.makedirs(test_dir)
    config.base_test_dir = test_dir
    # timeout = 60
    # start_time = time()
    # subprocess.Popen(["sudo", "docker-compose", "up"])
    # while time() - start_time < timeout:
    #     try:
    #         requests.get(url="http://0.0.0.0:8080/")
    #         break
    #     except:
    #         pass
    # else:
    #     print(f'Application did not start for {timeout} sec')


# def pytest_unconfigure():
#     subprocess.Popen(["sudo", "docker-compose", "down"])

@pytest.fixture(scope='session')
def mysql_client(request):
    client = request.config.mysql_client
    yield client
    client.connection.close()


@pytest.fixture(scope='function')
def driver(config, get_driver):
    get_driver.get(config['url'])
    yield get_driver
    get_driver.quit()


@pytest.fixture(scope='function')
def get_driver(config):
    if config["selenoid"] is not None:
        capabilities = {
            "browserName": "chrome",
            "browserVersion": "97.0",
            'additionalNetworks': ["selenoid"],
            # "applicationContainers": [f"{config['url']}:myapp"],
            "selenoid:options": {
                "enableVNC": True,
                "enableVideo": True
            }
        }
        browser = webdriver.Remote(command_executor=config["selenoid"], desired_capabilities=capabilities)
        # browser = webdriver.Remote(command_executor=config['url'], desired_capabilities=capabilities)
    else:
        os.environ['WDM_LOG_LEVEL'] = '0'
        manager = ChromeDriverManager(version='latest')
        browser = webdriver.Chrome(executable_path=manager.install())

    browser.maximize_window()
    return browser


repo_root = os.path.dirname(__file__)


@pytest.fixture(scope='function')
def test_dir(request, config):
    test_name = request._pyfuncitem.nodeid.replace(':', '_').replace('/', '_')
    # test_name = request.node.name
    dir_for_test = os.path.join(request.config.base_test_dir, test_name)
    os.makedirs(dir_for_test)
    return dir_for_test


@pytest.fixture(scope='function')
def logger(config, test_dir):
    log_formatter = logging.Formatter('%(asctime)s - %(filename)s - %(levelname)s: %(message)s')
    log_file = os.path.join(test_dir, 'test.log')
    log_level = logging.DEBUG if config['debug_log'] else logging.INFO

    file_handler = logging.FileHandler(log_file, 'w')
    file_handler.setFormatter(log_formatter)
    file_handler.setLevel(log_level)

    log = logging.getLogger('test')
    log.propagate = False
    log.setLevel(log_level)
    log.addHandler(file_handler)

    yield log

    for handler in log.handlers:
        handler.close()

    with open(log_file, 'r') as f:
        allure.attach(f.read(), 'test.log', attachment_type=allure.attachment_type.TEXT)

