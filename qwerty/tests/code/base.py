from api_client import ApiClient
import pytest


class BaseCase:

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, driver, config):
        self.driver = driver
        self.api_client = ApiClient(host='http://myapp_proxy:8070', username="testtest1", passwd="qwerty2")
