from ui.pages.base_page import BasePage
from ui.locators.main_page import MainPageLocators
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import allure


class MainPage(BasePage):

    locators = MainPageLocators()

    def open_page(self, title):
        elem = self.find(self.locators.navbar[title])
        locator = self.locators.navbar[title]
        parent_locator = (locator[0], locator[1] + '/..//li/a')
        links = self.driver.find_elements(*parent_locator)
        if not links:
            elem.send_keys(Keys.LEFT_CONTROL + Keys.ENTER)
            return
        elem.send_keys(Keys.NULL)
        for link in links:
            link.send_keys(Keys.LEFT_CONTROL + Keys.ENTER)


