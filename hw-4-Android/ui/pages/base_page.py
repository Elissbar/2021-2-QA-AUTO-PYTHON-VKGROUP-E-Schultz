from selenium.common.exceptions import StaleElementReferenceException, TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from appium.webdriver.common.touch_action import TouchAction
from ui.locators.base_locators import BasePageLocators

CLICK_RETRY = 3


class BasePage(object):
    locators = BasePageLocators()

    def __init__(self, driver, config):
        self.driver = driver
        self.config = config

    def find(self, locator, timeout=5):
        return self.wait(timeout).until(EC.presence_of_element_located(locator))

    def wait(self, timeout=5):
        return WebDriverWait(self.driver, timeout=timeout)

    def click(self, locator, timeout=5):
        for i in range(CLICK_RETRY):
            try:
                element = self.wait(timeout).until(EC.element_to_be_clickable(locator))
                element.click()
                return
            except StaleElementReferenceException:
                if i == CLICK_RETRY - 1:
                    raise

    def swipe_up(self, swipetime=200):
        action = TouchAction(self.driver)
        dimension = self.driver.get_window_size()
        x = int(dimension['width'] / 2)
        start_y = int(dimension['height'] * 0.8)
        end_y = int(dimension['height'] * 0.2)
        action.press(x=x, y=start_y).wait(ms=swipetime).move_to(x=x, y=end_y).release().perform()

    def swipe_to_element(self, locator, max_swipes=3):
        already_swiped = 0
        while len(self.driver.find_elements(*locator)) == 0:
            if already_swiped > max_swipes:
                raise TimeoutException(f"Error with {locator}, please check function")
            self.swipe_up()
            already_swiped += 1

    def swipe_element_lo_left(self, locator):
        web_element = self.find(locator, 10)
        action = TouchAction(self.driver)
        upper_y = web_element.location['y']
        lower_y = upper_y + web_element.rect['height']
        middle_y = (upper_y + lower_y) / 2
        # Не самый лучший, но вроде рабочий способ
        action.press(web_element).wait(ms=500).move_to(x=-500, y=middle_y).release().perform()

