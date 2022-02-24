from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ES
import logging


CLICK_RETRY = 3


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.logger = logging.getLogger('test')

        self.logger.info(f'Page is open: {self.__class__.__name__}')

    def wait(self, timeout=5):
        return WebDriverWait(self.driver, timeout)

    def find(self, locator):
        self.logger.info(f'Wait and find element: {locator}')
        return self.wait().until(ES.presence_of_element_located(locator))

    def click(self, locator):
        self.logger.info(f'Click on element: {locator}')
        for i in range(CLICK_RETRY):
            try:
                elem = self.wait().until(ES.element_to_be_clickable(locator))
                elem.click()
                return
            except:
                if i + 1 == CLICK_RETRY:
                    raise


