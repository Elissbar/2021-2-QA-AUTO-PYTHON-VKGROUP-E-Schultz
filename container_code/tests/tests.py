from base import BaseCase
from selenium.webdriver.support import expected_conditions as ES
import json
import pytest
import time


# @pytest.mark.test
# class TestTest(BaseCase):
#
#     only_auth = False
#
#     def test_google(self):
#         time.sleep(20)


@pytest.mark.api
class TestApi(BaseCase):

    only_auth = True

    def test_delete_user(self, create_user):
        user = create_user
        self.login_page.click(self.login_page.locators.log_out)
        self.login_page.registration_user(*user[:-1])
        assert self.api_client.get_delete(username=user[0]).status_code == 204

    def test_add_user(self, create_user):
        user = create_user[:-1]
        assert self.api_client.post_add_user(*user).status_code == 201

    def test_app_state(self):
        assert json.loads(self.api_client.get_app_state().content)["status"] == "ok"

    def test_block_user(self, create_user):
        user = create_user
        self.login_page.click(self.login_page.locators.log_out)
        self.login_page.registration_user(*user[:-1])
        self.api_client.get_block_user(username=user[0])
        query = f'select access from test_users where username="{user[0]}";'
        access_state = self.mysql.execute_query(query=query)
        assert access_state[0][0] == 0

    def test_unblock_user(self, create_user):
        user = create_user
        self.login_page.click(self.login_page.locators.log_out)
        self.login_page.registration_user(*user[:-1])
        self.api_client.get_block_user(username=user[0])
        self.api_client.get_unblock_user(username=user[0])
        query = f'select access from test_users where username="{user[0]}";'
        access_state = self.mysql.execute_query(query=query)
        assert access_state[0][0] == 1


@pytest.mark.reg
class TestRegistration(BaseCase):

    only_auth = False

    def test_valid(self, create_user, test_dir):
        user = create_user
        self.login_page.registration_user(username=user[0], password=user[1], email=user[2])
        username = self.main_page.find(self.main_page.locators.username).text
        vk_id = self.main_page.find(self.main_page.locators.vk_id).text
        assert json.loads(user[3])['vk_id'] in vk_id
        assert user[0] in username

    def test_invalid_login(self, create_user):
        user = create_user
        self.login_page.registration_user(username='qwert', password=user[1], email=user[2])
        locator = self.login_page.locators.error_message
        error_message = self.login_page.wait().until(ES.text_to_be_present_in_element(locator, 'Incorrect username length'))
        assert error_message

    def test_empty_email(self, create_user):
        user = create_user
        self.login_page.registration_user(username=user[0], password=user[1], email='')
        locator = self.login_page.locators.error_message
        error_message = self.login_page.wait().until(ES.text_to_be_present_in_element(locator, 'Incorrect email length'))
        assert error_message


@pytest.mark.auth
class TestAuthentication(BaseCase):

    only_auth = False

    def test_valid_login(self, request, create_user):
        user = request.getfixturevalue('register_user')[2]
        self.login_page.authorization_user(*user[0:2])
        username = self.main_page.find(self.main_page.locators.username).text
        vk_id = self.main_page.find(self.main_page.locators.vk_id).text
        assert user[0] in username
        assert json.loads(user[2])['vk_id'] in vk_id

    def test_invalid_login(self, request, create_user):
        user = request.getfixturevalue('register_user')[2]
        self.login_page.authorization_user(username='asdfds', password=user[1])
        locator = self.login_page.locators.error_message
        error_message = self.login_page.wait().until(ES.text_to_be_present_in_element(locator, 'Invalid username or password'))
        assert error_message

    def test_empty_password(self, request, create_user):
        user = request.getfixturevalue('register_user')[2]
        self.login_page.authorization_user(username=user[0], password='')
        assert '/welcome' not in self.driver.current_url


@pytest.mark.main_tests
class TestMainPage(BaseCase):

    only_auth = True

    @pytest.mark.parametrize(
        "title, url",
        [
            ('api', 'https://en.wikipedia.org/wiki/API'),
            ('foi', 'https://www.popularmechanics.com/technology/infrastructure/a29666802/future-of-the-internet/'),
            ('smtp', 'https://ru.wikipedia.org/wiki/SMTP')
        ])
    def test_open_link(self, title, url):
        self.main_page.click(self.main_page.locators.icons[title])
        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[1])
        assert self.driver.current_url == url

    @pytest.mark.parametrize(
        "title, urls",
        [
            ('home', ['http://0.0.0.0:8081/welcome/']),
            ('python', ['https://en.wikipedia.org/wiki/History_of_Python', 'https://flask.palletsprojects.com/en/1.1.x/#']),
            ('linux', ['https://getfedora.org/ru/workstation/download/']),
            ('network', ['https://www.wireshark.org/news/', 'https://www.wireshark.org/#download', 'https://hackertarget.com/tcpdump-examples/'])
        ]
    )
    def test_open_link_in_navbar(self, title, urls):
        self.main_page.open_page(title)
        assert all(self.check_url(data=urls))
