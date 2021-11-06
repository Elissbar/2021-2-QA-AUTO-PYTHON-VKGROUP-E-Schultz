from ui.pages.login_page import LoginPage
from ui.pages.campaign_page import CampaignPage
from _pytest.fixtures import FixtureRequest
from base import BaseCase
import allure
import pytest


@pytest.mark.UI
class TestInvalidCase(BaseCase):
    authorize = False

    @allure.story('Negative tests')
    def test_invalid_login(self):
        login_page = LoginPage(self.driver)
        login_page.login(login='qawsed@gmail.ru', password='kirito4789')
        assert self.driver.current_url != "https://target.my.com/dashboard"

    @allure.story('Negative tests')
    def test_invalid_password(self):
        login_page = LoginPage(self.driver)
        login_page.login(login="allen-2002@mail.ru", password=' ')
        assert self.driver.current_url != "https://target.my.com/dashboard"


@pytest.mark.UI
class TestCreation(BaseCase):
    authorize = True

    @allure.story('Positive tests')
    def test_create_campaign(self, file_path, fake_data):
        campaign = CampaignPage(self.driver)
        campaign_name = campaign.create_campaign(file_path, *fake_data)
        assert campaign_name in self.driver.page_source
        campaign.delete_campaign(campaign_name)

    @allure.story('Positive tests')
    def test_create_segment(self, request: FixtureRequest, fake_data):
        segments_page = request.getfixturevalue('get_page')
        link_text = segments_page.create_segment(name=fake_data[0])
        assert segments_page.check_segment(link_text)
        segments_page.delete_segment(link_text)

    @allure.story('Positive tests')
    def test_delete_segment(self, request: FixtureRequest, fake_data):
        segments_page = request.getfixturevalue('get_page')
        link_text = segments_page.create_segment(name=fake_data[0])
        segments_page.delete_segment(link_text)
        assert not segments_page.check_segment(link_text)
