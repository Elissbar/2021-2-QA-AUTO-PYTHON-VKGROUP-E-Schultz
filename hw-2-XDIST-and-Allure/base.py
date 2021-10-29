from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from _pytest.fixtures import FixtureRequest
from ui.pages.base_page import BasePage
from ui.pages.login_page import LoginPage
from faker import Faker
import allure
import time
import pytest
import os


class BaseCase:
    authorize = True

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, driver, request: FixtureRequest, logger):
        self.driver = driver
        self.logger = logger

        if self.authorize:
            cookies = request.getfixturevalue('cookies')
            for cookie in cookies:
                self.driver.add_cookie(cookie)
            self.driver.refresh()
        self.base_page = BasePage(driver=driver)

    @pytest.fixture(scope='session')
    def credentials(self):
        with open('credentials.txt', "r") as f:
            login = f.readline().strip()
            password = f.readline().strip()
            return login, password


    @pytest.fixture(scope='session')
    def cookies(self, config, credentials):
        os.environ['WDM_LOG_LEVEL'] = '0'
        manager = ChromeDriverManager(version='latest')
        driver = webdriver.Chrome(executable_path=manager.install())
        driver.get(config['url'])
        login_page = LoginPage(driver)
        login_page.login(*credentials)
        cookies = driver.get_cookies()
        driver.quit()
        return cookies

    @pytest.fixture(scope='function')
    def fake_data(self):
        faker = Faker()
        start_time = time.time()
        fake_title = faker.lexify(text='?????? ??? ???')
        name = str(start_time) + faker.numerify(text=f'{fake_title} ###%#%#%')
        url = faker.image_url()
        self.logger.info('Generate fake data for test')
        return name, url

