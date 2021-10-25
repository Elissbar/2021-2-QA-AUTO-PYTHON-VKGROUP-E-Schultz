from selenium.webdriver.support import expected_conditions as ES
from base import BaseCase
from faker import Faker
import pytest


@pytest.mark.UI
class TestSuite(BaseCase):
    fake = Faker()

    def test_log_in(self, login):
        assert self.base_page.wait().until(ES.element_to_be_clickable(self.base_page.locators.create_campaign_btn))

    def test_log_out(self, login):
        self.base_page.log_out()
        assert self.base_page.wait().until(ES.element_to_be_clickable(self.base_page.locators.log_in['log_in']))

    def test_change_contact_info(self, login):
        name = self.fake.name()
        phone = self.fake.phone_number()
        self.base_page.find(self.base_page.locators.tabs["profile"]).click()
        self.profile_page.save_change(name, phone)
        assert self.base_page.find(self.profile_page.locators.full_name).get_attribute('value') == name
        assert self.base_page.find(self.profile_page.locators.phone_number).get_attribute('value') == phone

    @pytest.mark.parametrize('tab, tab_url', [('tools', 'https://target.my.com/tools/feeds'), ('segments', 'https://target.my.com/segments/segments_list')])
    def test_move_to_tab(self, login, tab, tab_url):
        self.base_page.find(self.base_page.locators.tabs[tab]).click()
        assert tab_url == self.driver.current_url
