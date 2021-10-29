from selenium.webdriver.support import expected_conditions as ES
from ui.pages.login_page import LoginPage
from ui.pages.segments_page import SegmentsPage
from ui.pages.campaign_page import CampaignPage
from base import BaseCase
import allure
import pytest


@pytest.mark.UI
class TestInvalidCase(BaseCase):
    authorize = False

    @allure.epic('PyTest with allure')
    @allure.feature('Log in with invalid data')
    @allure.story('Negative tests')
    def test_invalid_login(self, credentials):
        self.logger.info('Enter invalid login')
        login_page = LoginPage(self.driver)
        login = 'qawsed@gmail.ru'
        with allure.step(f'Enter invalid login: {login}'):
            login_page.login(login, credentials[1])
        error_message = self.base_page.find(self.base_page.locators.invalid_login_page['error_message'])
        error_title = error_message.find_element(*self.base_page.locators.invalid_login_page['error_title']).text
        error_text = error_message.find_element(*self.base_page.locators.invalid_login_page['error_text']).text
        self.logger.info(f'Assert error message: {error_text}')
        with allure.step('Assert title and error text'):
            assert "Error" == error_title
            assert "Invalid login or password" == error_text

    @allure.epic('PyTest with allure')
    @allure.feature('Log in with invalid data')
    @allure.story('Negative tests')
    def test_invalid_password(self, credentials):
        self.logger.info('Enter invalid password')
        login_page = LoginPage(self.driver)
        password = ' '
        with allure.step(f'Enter invalid password: {password}'):
            login_page.login(credentials[0], password)
        self.logger.info('Assert error message - "Invalid password format"')
        with allure.step('Password is invalid'):
            assert self.base_page.wait().until(ES.text_to_be_present_in_element(
                self.base_page.locators.invalid_password,
                 'Invalid password format'
            ))


@pytest.mark.UI
class TestCreation(BaseCase):
    authorize = True

    @allure.epic('PyTest with allure')
    @allure.feature('Create and delete testing')
    @allure.story('Positive tests')
    def test_create_campaign(self, file_path, fake_data):
        campaign = CampaignPage(self.driver)
        with allure.step('Create campaign'):
            campaign_name = campaign.create_campaign(file_path, *fake_data)
        with allure.step('Check campaign in page'):
            assert campaign_name in self.driver.page_source
        with allure.step('Delete campaign'):
            campaign.delete_campaign(campaign_name)

    @allure.epic('PyTest with allure')
    @allure.feature('Create and delete testing')
    @allure.story('Positive tests')
    def test_create_segment(self, fake_data):
        self.base_page.click(self.base_page.locators.tabs['segments'])
        segments_page = SegmentsPage(self.driver)
        with allure.step('Create segment'):
            link_text = segments_page.create_segment(name=fake_data[0])
        with allure.step('Check segment in page'):
            assert link_text in self.driver.page_source
        with allure.step('Delete segment'):
            segments_page.delete_segment(link_text)

    @allure.epic('PyTest with allure')
    @allure.feature('Create and delete testing')
    @allure.story('Positive tests')
    def test_delete_segment(self, fake_data):
        self.base_page.click(self.base_page.locators.tabs['segments'])
        segments_page = SegmentsPage(self.driver)
        with allure.step('Create segment'):
            link_text = segments_page.create_segment(name=fake_data[0])
        with allure.step('Delete segment'):
            deleted_segment = segments_page.delete_segment(link_text)
        with allure.step('Check deleted segment in page'):
            assert deleted_segment not in self.driver.page_source
