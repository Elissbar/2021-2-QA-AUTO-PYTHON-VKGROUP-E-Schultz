from ui.pages.profile_page import ProfilePage
from ui.pages.base_page import BasePage
import pytest

EMAIL = "allen-2002@mail.ru"
PASS = "kirito4789"


class BaseCase:

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, driver):
        self.driver = driver

        self.base_page = BasePage(driver=driver)
        self.profile_page = ProfilePage(driver=driver)

    @pytest.fixture(scope='function')
    def login(self):
        self.base_page.find(self.base_page.locators.log_in['log_in']).click()
        self.base_page.find(self.base_page.locators.log_in['email']).send_keys(EMAIL)
        self.base_page.find(self.base_page.locators.log_in['password']).send_keys(PASS)
        self.base_page.find(self.base_page.locators.log_in['submit']).click()
        self.base_page.find(self.base_page.locators.create_campaign_btn)








