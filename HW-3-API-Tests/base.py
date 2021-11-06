from client import ApiClient
from _pytest.fixtures import FixtureRequest
from payloads.create_campaign import Payloads
from urllib.parse import urljoin
from faker import Faker
import pytest
import os


class BaseCase:
    authorize = True

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, request: FixtureRequest):
        self.api_client = ApiClient('https://target.my.com/')
        self.payloads = Payloads()

        if self.authorize:
            credentials = request.getfixturevalue('credentials')
            self.api_client.post_login(*credentials)

    @pytest.fixture(scope='session')
    def credentials(self, repo_root):
        with open(os.path.join(repo_root, 'credentials.txt'), "r") as f:
            login = f.readline().strip()
            password = f.readline().strip()
            return login, password

    @pytest.fixture(scope='function')
    def fake_data(self):
        faker = Faker()
        name = faker.lexify(text='????????????')
        return name

    @pytest.fixture(scope='function')
    def post_create_campaign(self, file_path, fake_data):
        file_id = self.api_client.post_upload_file(file_path)
        location = 'api/v2/campaigns.json'
        headers = {
            'X-CSRFToken': self.api_client.csrf_token
        }
        payload = self.payloads.campaign_payload(campaign_name=fake_data, file_id=file_id)
        result = self.api_client.session.post(urljoin(self.api_client.base_url, location), headers=headers, json=payload)
        yield result.json()['id']
        location = f'api/v2/campaigns/{result.json()["id"]}.json'
        headers = {
            'X-CSRFToken': self.api_client.csrf_token
        }
        return self.api_client.session.delete(urljoin(self.api_client.base_url, location), headers=headers)




