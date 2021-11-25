import pytest
from ui.pages.base_page import BasePage
from ui.pages.settings_page import SettingsPage
from ui.pages.command_page import CommandPage


class BaseCase:

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, driver, config):
        self.driver = driver
        self.config = config

        self.base_page = BasePage(self.driver, self.config)
        self.settings_page = SettingsPage(self.driver, self.config)
        self.command_page = CommandPage(self.driver, self.config)
