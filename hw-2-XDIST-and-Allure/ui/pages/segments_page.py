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
            self.find(self.locators.first_button).click()
        except:
            self.find(self.locators.create_segment).click()
        finally:
            self.click(self.locators.apps_and_games)
            self.click(self.locators.checkbox)
            self.click(self.locators.add_segment)
            self.logger.info(f'Paste segment name: {name}')
            name_segment = self.find(self.locators.name_segment)
            self.clear_inputs(name_segment).send_keys(f'{name}')
            self.logger.info(f'Creation segment')
            self.click(self.locators.create_segment)
            created_segment = self.find(self.locators.segment_link(name)).text
            return created_segment

    @allure.step('Delete segment')
    def delete_segment(self, name_segment):
        self.logger.info(f'Delete segment with name: {name_segment}')
        segment_link = self.find(self.locators.segment_link(name_segment)).get_attribute('href')
        segment_id = re.findall(r'\d+', segment_link)[0]
        self.logger.info(f'Get id segment: {segment_id}')
        self.click(self.locators.delete_segment(segment_id))
        self.click(self.locators.confirm_remove)
        self.driver.refresh()

    @allure.step('Check segment')
    def check_segment(self, name_segment):
        try:
            self.find(self.locators.segment_link(name_segment))
            self.logger.info(f'Segment in page')
            return True
        except:
            self.logger.info(f'Segment not in page')
            return False
