from ui.pages.base_page import BasePage
from ui.locators.main_page import MainPageLocators
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import allure


class MainPage(BasePage):

    locators = MainPageLocators()

    def open_page(self, title):
        pass
        # action = ActionChains(self.driver)
        # locator = self.locators.navbar[title]
        # parent_locator = (locator[0], locator[1] + '/..//li/a')
        # self.find(self.locators.navbar[title]).send_keys(Keys.NULL)
        # links = self.driver.find_elements(*parent_locator)
        # for link in links:
        #     action.key_down(Keys.CONTROL).click(link).key_up(Keys.CONTROL).perform()


