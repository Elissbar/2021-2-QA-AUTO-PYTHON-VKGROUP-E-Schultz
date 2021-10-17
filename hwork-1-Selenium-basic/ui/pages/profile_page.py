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

    def save_change(self):
        self.clear_inputs(self.find(self.locators.full_name)).send_keys('Shultz Eduard')
        self.clear_inputs(self.find(self.locators.phone_number)).send_keys('+71111111111')

        self.find(self.locators.save_change_btn).click()

        assert 'Information saved successfully' in self.driver.page_source # заменить на is_displaed
