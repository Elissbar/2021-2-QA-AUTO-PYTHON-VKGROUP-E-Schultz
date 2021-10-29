from selenium.webdriver.support import expected_conditions as ES
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from ui.locators.base_locators import BasePageLocators
from selenium.common.exceptions import StaleElementReferenceException
from sys import platform
import allure
import logging


CLICK_RETRY = 3


class BasePage:
    locators = BasePageLocators()

    def __init__(self, driver):
        self.driver = driver
        self.logger = logging.getLogger('test')
        self.logger.info(f'{self.__class__.__name__} page is opening')

    def wait(self, timeout=10):
        self.logger.info(f'Waiting an item. Timeout is: {timeout}')
        return WebDriverWait(self.driver, timeout)

    def find(self, locator, timeout=10):
        self.logger.info(f'Find item with locator: {locator}')
        return self.wait(timeout).until(ES.presence_of_element_located(locator))

    def move_to_element(self, element):
        self.logger.info(f'Move to element: {element}')
        action = ActionChains(self.driver)
        return action.move_to_element(element).perform()

    @allure.step('Logout')
    def log_out(self):
        self.click(self.locators.right_menu)
        self.click(self.locators.log_out)

    def click(self, locator):
        self.logger.info(f'Click on locator: {locator}')
        for i in range(CLICK_RETRY):
            try:
                self.find(locator)
                elem = self.wait().until(ES.element_to_be_clickable(locator))
                self.move_to_element(elem)
                elem.click()
                return
            except StaleElementReferenceException:
                if i == CLICK_RETRY-1:
                    raise

    @allure.step('Clear input')
    def clear_inputs(self, elem):
        key = Keys.CONTROL
        if platform == 'darwin':
            key = Keys.COMMAND
        elem.send_keys(key + 'a')
        elem.send_keys(Keys.DELETE)
        return elem

