from selenium.webdriver.support import expected_conditions as ES
from ui.locators.profile_locators import ProfilePageLocators
from selenium.webdriver.common.keys import Keys
from ui.pages.base_page import BasePage


class ProfilePage(BasePage):
    locators = ProfilePageLocators()

    @staticmethod
    def clear_inputs(elem):
        elem.send_keys(Keys.CONTROL + 'a')
        elem.send_keys(Keys.DELETE)
        return elem

    def save_change(self, name, phone):
        self.clear_inputs(self.find(self.locators.full_name)).send_keys(name)
        self.clear_inputs(self.find(self.locators.phone_number)).send_keys(phone)
        self.find(self.locators.save_change_btn).click()
        self.driver.refresh()
        self.wait().until(ES.element_to_be_clickable(self.locators.save_change_btn))
