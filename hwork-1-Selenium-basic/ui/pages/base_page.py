from selenium.webdriver.support import expected_conditions as ES
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from ui.locators.base_locators import BasePageLocators


class BasePage:
    locators = BasePageLocators()

    def __init__(self, driver):
        self.driver = driver

    def wait(self, timeout=10):
        return WebDriverWait(self.driver, timeout)

    def find(self, locator, timeout=10):
        return self.wait(timeout).until(ES.presence_of_element_located(locator))

    def move_to_element(self, element):
        action = ActionChains(self.driver)
        return action.move_to_element(element).perform()

    def log_out(self):
        self.find(self.locators.right_menu).click()
        log_out = self.find(self.locators.log_out)
        self.move_to_element(log_out)
        log_out.click()
        self.find(self.locators.h1)
