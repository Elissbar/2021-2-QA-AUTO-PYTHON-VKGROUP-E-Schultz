from selenium.webdriver.support import expected_conditions as ES
from base import BaseCase
import pytest


@pytest.mark.UI
class TestSuite(BaseCase):

    def test_log_in(self, login):
        assert self.base_page.wait().until(ES.title_is('Campaigns'))

    def test_log_out(self, login):
        self.base_page.log_out()
        assert self.base_page.wait().until(ES.title_is('MyTarget platform — targeted advertising service'))

    def test_change_contact_info(self, login):
        self.base_page.find(self.base_page.locators.tabs["profile"]).click()
        self.profile_page.save_change()

    @pytest.mark.parametrize('tab, title', [('tools', 'Feeds list'), ('segments', 'Segments list')])
    def test_move_to_tab(self, login, tab, title):
        self.base_page.find(self.base_page.locators.tabs[tab]).click()
        assert self.base_page.wait(timeout=2).until(ES.title_is(title))
