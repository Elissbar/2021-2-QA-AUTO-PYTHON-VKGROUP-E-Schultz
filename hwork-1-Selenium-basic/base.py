from ui.pages.profile_page import ProfilePage
from ui.pages.base_page import BasePage
import pytest


class BaseCase:
    @pytest.fixture(scope='function', autouse=True)
    def setup(self, driver):
        self.driver = driver
        self.base_page = BasePage(driver=driver)
        self.profile_page = ProfilePage(driver=driver)

    @pytest.fixture(scope='function')
    def login(self):
        with open('credentials.txt', "r") as file:
            login = file.readline().strip()
            password = file.readline().strip()
        self.base_page.find(self.base_page.locators.log_in['log_in']).click()
        self.base_page.find(self.base_page.locators.log_in['email']).send_keys(login)
        self.base_page.find(self.base_page.locators.log_in['password']).send_keys(password)
        self.base_page.find(self.base_page.locators.log_in['submit']).click()
        self.base_page.find(self.base_page.locators.create_campaign_btn)
