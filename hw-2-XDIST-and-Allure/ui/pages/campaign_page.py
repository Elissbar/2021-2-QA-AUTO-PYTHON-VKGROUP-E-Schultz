from ui.locators.campaign_locators import CampaignPageLocators
from selenium.webdriver.support import expected_conditions as ES
from ui.pages.base_page import BasePage
import allure


class CampaignPage(BasePage):
    locators = CampaignPageLocators()

    @allure.step('Create Campaign')
    def create_campaign(self, file_path, name, url):
        try:
            create_campaign_btn = self.find(self.locators.create_campaign_btn, timeout=2)
            self.logger.info(f'Click on "create_campaign_btn" to create campaign": {create_campaign_btn}')
            create_campaign_btn.click()
        except:
            button_wrap = self.find(self.locators.button_wrap)
            create_campaign = button_wrap.find_element(*self.locators.create_button_in_wrap)
            self.logger.info(f'Click on "create_campaign" to create campaign": {create_campaign}')
            create_campaign.click()
        finally:
            self.click(self.locators.traffic)
            self.find(self.locators.input_url).send_keys(url)
            name_campaign = self.wait().until(ES.element_to_be_clickable(self.locators.name_campaign))
            self.move_to_element(name_campaign)
            self.clear_inputs(name_campaign).send_keys(name)
            self.click(self.locators.banner)
            wrap_upload = self.wait().until(ES.element_to_be_clickable(self.locators.wrap_upload))
            self.move_to_element(wrap_upload)
            try:
                self.find(self.locators.remove_all, timeout=2).click()
            except:
                pass
            try:
                self.find(self.locators.confirm_remove, timeout=2).click()
            except:
                pass
            self.find(self.locators.upload_file).send_keys(file_path)
            self.find(self.locators.edit_the_image_window)
            self.click(self.locators.save_image)
            self.click(self.locators.create_a_campaign)
            self.click(self.locators.select_status_campaign)
            self.click(self.locators.active_campaigns)
            return name

    @allure.step('Delete Campaign')
    def delete_campaign(self, campaign_name):
        campaign_list = self.driver.find_elements(*self.locators.campaign_list)
        self.logger.info(f'Count of campaign": {len(campaign_list)}')
        for i in range(1, len(campaign_list)):
            link_campaign = self.find((self.locators.link_campaign[0], self.locators.link_campaign[1].format(i)))
            checkbox_campaign = self.find((self.locators.checkbox_campaign[0], self.locators.checkbox_campaign[1].format(i)))
            if link_campaign.text == campaign_name:
                checkbox_campaign.click()
                self.click(self.locators.select_action)
                self.logger.info(f'Delete campaign with name": {campaign_name}')
                self.click(self.locators.delete_action)
                self.driver.refresh()
                self.wait().until(ES.element_to_be_clickable(self.locators.button_wrap))
                break
        assert campaign_name not in self.driver.page_source
