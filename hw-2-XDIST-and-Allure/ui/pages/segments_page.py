from ui.locators.segments_locator import SegmentsPageLocator
from ui.pages.base_page import BasePage
import allure
import re


class SegmentsPage(BasePage):
    locators = SegmentsPageLocator()

    @allure.step('Create segment')
    def create_segment(self, name):
        self.logger.info(f'Creation segment with name: {name}')
        try:
            self.find(self.locators.FIRST_BUTTON).click()
        except:
            self.find(self.locators.CREATE_SEGMENT).click()
        self.click(self.locators.APPS_AND_GAMES)
        self.click(self.locators.CHECKBOX)
        self.click(self.locators.ADD_SEGMENT)
        self.logger.info(f'Paste segment name: {name}')
        name_segment = self.find(self.locators.NAME_SEGMENT)
        self.clear_inputs(name_segment).send_keys(f'{name}')
        self.logger.info(f'Creation segment')
        self.click(self.locators.CREATE_SEGMENT)
        created_segment = self.find(self.locators.SEGMENT_LINK(name)).text
        return created_segment

    @allure.step('Delete segment')
    def delete_segment(self, name):
        self.logger.info(f'Delete segment with name: {name}')
        segment_link = self.find(self.locators.SEGMENT_LINK(name)).get_attribute('href')
        segment_id = re.findall(r'\d+', segment_link)[0]
        self.logger.info(f'Get id segment: {segment_id}')
        self.click(self.locators.DELETE_SEGMENT(segment_id))
        self.click(self.locators.CONFIRM_REMOVE)
        self.logger.info(f'Segment is deleted')
        self.driver.refresh()

    @allure.step('Check segment')
    def check_segment(self, name):
        try:
            self.find(self.locators.SEGMENT_LINK(name))
            self.logger.info(f'Segment in page')
            return True
        except:
            self.logger.info(f'Segment not in page')
            return False
