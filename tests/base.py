from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from api_client.api_client import ApiClient
from orm.client import MySQLClient
from ui.pages.login_page import LoginPage
from ui.pages.main_page import MainPage
import pytest
import requests
from faker import Faker
import os


class BaseCase:

    only_auth = None

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, driver, config, request, logger):
        self.driver = driver
        self.faker = Faker()
        self.logger = logger
        self.mysql = MySQLClient(host=config['mysql'], db='TEST')

        if self.only_auth:
            cookies = request.getfixturevalue('cookies')[0]
            agent = request.getfixturevalue('cookies')[1]
            for cookie in cookies:
                self.driver.add_cookie({'name': cookie['name'], 'value': cookie['value']})
            self.driver.refresh()
            self.api_client = ApiClient(host=config['url'], cookies=cookies[0], agent=agent)

        self.login_page = LoginPage(self.driver)
        self.main_page = MainPage(self.driver)

    @pytest.fixture(scope='session')
    def cookies(self, config):
        os.environ['WDM_LOG_LEVEL'] = '0'
        manager = ChromeDriverManager(version='latest')
        driver = webdriver.Chrome(executable_path=manager.install())
        driver.get(config['url'])
        login_page = LoginPage(driver)
        login_page.registration_user(username="testuser", email="qwerty@qwerty.ru", password="qwerty2")
        cookies = driver.get_cookies()
        agent = driver.execute_script("return navigator.userAgent")
        driver.quit()
        return cookies, agent

    @pytest.fixture(scope='function')
    def create_user(self, config):
        user = self.faker.profile()
        password = self.faker.bothify(text='???#??##')
        username = user['username']
        email = user['mail']
        user_id = requests.post(f'{config["mock"]}/add_user/{username}').content
        return username, password, email, user_id
