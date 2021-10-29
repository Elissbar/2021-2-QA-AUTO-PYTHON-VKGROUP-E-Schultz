from ui.locators.segments_locator import SegmentsPageLocator
from ui.pages.base_page import BasePage
import allure


class SegmentsPage(BasePage):
    locators = SegmentsPageLocator()

    @allure.step('Create segment')
    def create_segment(self, name):
        try:
            self.find(self.locators.first_button).click()
        except:
            self.find(self.locators.create_segment).click()
        finally:
            self.click(self.locators.apps_and_games)
            self.click(self.locators.checkbox)
            self.click(self.locators.add_segment_button)
            name_segment = self.find(self.locators.name_segment)
            self.clear_inputs(name_segment).send_keys(f'{name}')
            self.find(self.locators.create_segment).click()
            created_segment = self.find(self.locators.segment_link).text
            return created_segment

    @allure.step('Delete segment')
    def delete_segment(self, name_segment):
        segments = self.driver.find_elements(*self.locators.segments_list)
        self.logger.info(f'Count of segments": {len(segments)}')
        for i in range(len(segments)):
            segment = self.find((self.locators.segment[0], self.locators.segment[1].format(i)))
            segment_link = segment.find_element(*self.locators.segment_link)
            if segment_link.text == name_segment:
                self.click((self.locators.remove[0], self.locators.remove[1].format(i)))
                self.click(self.locators.delete)
                self.logger.info(f'Delete segment with name": {name_segment}')
                self.driver.refresh()
                break
        assert name_segment not in self.driver.page_source
        return name_segment
