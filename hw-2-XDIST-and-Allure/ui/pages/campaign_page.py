from ui.locators.campaign_locators import CampaignPageLocators
from ui.pages.base_page import BasePage
import allure
import re


class CampaignPage(BasePage):
    locators = CampaignPageLocators()

    @allure.step('Create Campaign')
    def create_campaign(self, file_path, name, url):
        self.logger.info(f'Creating new campaign with URL: {url} and Name: {name}')
        try:
            self.click(self.locators.FIRST_CREATE)
            self.logger.info(f'Creating new campaign first time')
        except:
            self.click(self.locators.NEXT_CREATE)
        self.logger.info(f'Choose campaign with traffic type')
        self.click(self.locators.TRAFFIC)
        self.logger.info(f'Paste url campaign')
        self.find(self.locators.IPNUT_URL).send_keys(url)
        name_campaign = self.is_clickable(self.locators.NAME_CAMPAIGN)
        self.logger.info(f'Move to input with name')
        self.move_to_element(name_campaign)
        self.clear_inputs(name_campaign).send_keys(name)
        self.logger.info(f'Click on banner type')
        self.click(self.locators.BANNER)
        self.logger.info(f'Move to input with name')
        self.move_to_element(self.is_clickable(self.locators.WRAP_UPLOAD))
        self.logger.info(f'Remove previous images')
        try:
            self.click(self.locators.REMOVE_FILE)
            self.click(self.locators.CONFIRM_REMOVE)
        except:
            pass
        self.logger.info(f'Paste image campaign')
        self.find(self.locators.UPLOAD_FILE).send_keys(file_path)
        self.click(self.locators.SAVE_IMAGE)
        self.click(self.locators.CREATE_A_CAMPAIGN)
        self.logger.info(f'Choose active campaigns')
        self.click(self.locators.SELECT_STATUS_CAMPAIGN)
        self.click(self.locators.ACTIVE_CAMPAIGNS)
        return name

    @allure.step('Delete Campaign')
    def delete_campaign(self, name):
        self.logger.info(f'Get link text campaign with name: {name}')
        campaign_link = self.find(self.locators.CAMPAIGN_LINK(name)).get_attribute('href')
        campaign_id = re.findall(r'\d+', campaign_link)[0]
        self.logger.info(f'Remove campaign with id: {campaign_id}')
        self.click(self.locators.CHECKBOX_TO_DELETE(campaign_id))
        self.click(self.locators.SELECT_ACTION)
        self.click(self.locators.DELETE_ACTION)
        self.driver.refresh()
