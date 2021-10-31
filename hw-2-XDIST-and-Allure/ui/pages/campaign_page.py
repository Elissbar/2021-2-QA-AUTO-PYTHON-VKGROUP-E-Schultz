from ui.locators.campaign_locators import CampaignPageLocators
from selenium.webdriver.support import expected_conditions as ES
from ui.pages.base_page import BasePage
import allure
import re


class CampaignPage(BasePage):
    locators = CampaignPageLocators()

    @allure.step('Create Campaign')
    def create_campaign(self, file_path, name, url):
        self.logger.info(f'Creating new campaign with URL: {url} and Name: {name}')
        try:
            self.click(self.locators.first_create)
            self.logger.info(f'Creating new campaign first time')
        except:
            self.click(self.locators.next_create)
        finally:
            self.logger.info(f'Choose campaign with traffic type')
            self.click(self.locators.traffic)
            self.logger.info(f'Paste url campaign')
            self.find(self.locators.input_url).send_keys(url)
            name_campaign = self.wait().until(ES.element_to_be_clickable(self.locators.name_campaign))
            self.logger.info(f'Move to input with name')
            self.move_to_element(name_campaign)
            self.clear_inputs(name_campaign).send_keys(name)
            self.logger.info(f'Click on banner type')
            self.click(self.locators.banner)
            self.logger.info(f'Move to input with name')
            self.move_to_element(self.wait().until(ES.element_to_be_clickable(self.locators.wrap_upload)))
            self.logger.info(f'Remove previous images')
            try:
                self.click(self.locators.remove_all)
                try:
                    self.click(self.locators.confirm_remove)
                except:
                    pass
            except:
                pass
            self.logger.info(f'Paste image campaign')
            self.find(self.locators.upload_file).send_keys(file_path)
            self.click(self.locators.save_image)
            self.click(self.locators.create_a_campaign)
            self.logger.info(f'Choose active campaigns')
            self.click(self.locators.select_status_campaign)
            self.click(self.locators.active_campaigns)
            return name

    @allure.step('Delete Campaign')
    def delete_campaign(self, name):
        self.logger.info(f'Get link text campaign with name: {name}')
        campaign_link = self.find(self.locators.campaign_link(name)).get_attribute('href')
        campaign_id = re.findall(r'\d+', campaign_link)[0]
        self.logger.info(f'Remove campaign with id: {campaign_id}')
        self.click(self.locators.checkbox_to_delete(campaign_id))
        self.click(self.locators.select_action)
        self.click(self.locators.delete_action)
        self.driver.refresh()
