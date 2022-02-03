from base import BaseCase
import json
import time
import pytest


class TestUser(BaseCase):

    only_auth = False

    @pytest.mark.parametrize('value', ['1-value', '2-value'])
    def test_registration_user(self, create_user, test_dir, value):
        user = create_user
        self.login_page.registration_user(username=user[0], password=user[1], email=user[2])
        time.sleep(10)
        username = self.main_page.get_user_data()[0]
        vk_id = self.main_page.get_user_data()[1]
        assert json.loads(user[3])['vk_id'] in vk_id
        assert user[0] in username

