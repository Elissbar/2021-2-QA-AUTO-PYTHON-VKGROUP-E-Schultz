from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
import logging
import pytest
import allure
import shutil
import os


def pytest_addoption(parser):
    parser.addoption("--browser", default="chrome")
    parser.addoption("--url", default="https://target.my.com/")
    parser.addoption('--debug_log', action='store_true')


@pytest.fixture(scope='session')
def config(request):
    browser = request.config.getoption("--browser")
    url = request.config.getoption("--url")
    debug_log = request.config.getoption('--debug_log')
    return { 'browser': browser, 'url': url, 'debug_log': debug_log }


def pytest_configure(config):
    base_test_dir = os.path.join('tmp', 'tests')
    if not hasattr(config, 'workerinput'):
        if os.path.exists(base_test_dir):
            shutil.rmtree(base_test_dir)
        os.makedirs(base_test_dir)
    config.base_test_dir = base_test_dir


@pytest.fixture(scope='function')
def test_dir(request):
    test_name = request._pyfuncitem.nodeid.replace('/', '_').replace(':', '_')
    test_dir = os.path.join(request.config.base_test_dir, test_name)
    os.makedirs(test_dir)
    return test_dir


@pytest.fixture(scope='function')
def driver(config):
    os.environ['WDM_LOG_LEVEL'] = '0'
    manager = ChromeDriverManager(version='latest')
    browser = webdriver.Chrome(executable_path=manager.install())
    browser.maximize_window()
    browser.get(config['url'])
    yield browser
    browser.quit()


@pytest.fixture(scope='function')
def file_path():
    return os.path.join(os.path.dirname(__file__), "target.png")


@pytest.fixture(scope='function')
def logger(config, test_dir):
    log_formatter = logging.Formatter('%(asctime)s - %(filename)-s - %(levelname)-s: %(message)s')
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


@pytest.fixture(scope='function', autouse=True)
def ui_report(driver, request, test_dir):
    failed_tests_count = request.session.testsfailed
    yield
    if request.session.testsfailed > failed_tests_count:
        screenshot_file = os.path.join(test_dir, 'failure.png')
        driver.get_screenshot_as_file(screenshot_file)
        allure.attach.file(screenshot_file, 'failure.png', attachment_type=allure.attachment_type.PNG)

        browser_logfile = os.path.join(test_dir, 'browser.log')
        with open(browser_logfile, 'w') as f:
            for i in driver.get_log('browser'):
                f.write(f"{i['level']} - {i['source']}\n{i['message']}\n\n")

        with open(browser_logfile, 'r') as f:
            allure.attach(f.read(), 'browser.log', attachment_type=allure.attachment_type.TEXT)

        log_file = os.path.join(test_dir, 'test.log')
        if os.path.exists(log_file):
            with open(log_file, 'r') as f:
                allure.attach(f.read(), 'test.log', attachment_type=allure.attachment_type.TEXT)
