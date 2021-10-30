from client import ApiClient
from _pytest.fixtures import FixtureRequest
from faker import Faker
import pytest
import os


class BaseCase:
    authorize = True

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, request: FixtureRequest):
        self.api_client = ApiClient()

        if self.authorize:
            credentials = request.getfixturevalue('credentials')
            self.api_client.login(*credentials)

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




