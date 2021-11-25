from ui.pages.base_page import BasePage
from ui.locators.command_locators import CommandPageLocators


class CommandPage(BasePage):
    locators = CommandPageLocators()

    def send_values(self, values):
        self.find(self.locators.search_input).send_keys(values)
        self.click(self.locators.search_submit)

    def get_chat_page(self, values):
        self.click(self.locators.search_button)
        self.send_values(values=values)
