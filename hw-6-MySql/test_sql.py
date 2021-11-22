from base import Base
from parse.parse_logs import *


class TestSQL(Base):

    def test_count_requests(self):
        count_requests = self.get_count_requests()
        assert count_requests[0].count == return_count_requests(self.path_to_log)

    def test_top_requests_type(self):
        top_requests = self.get_top_requests()
        assert len(top_requests) == len(count_requests_with_type(self.path_to_log))

    def test_frequent_requests(self):
        frequent_requests = self.get_frequent_url()
        assert len(frequent_requests) == len(get_url(self.path_to_log))

    def test_client_error(self):
        client_errors = self.get_client_errors()
        assert len(client_errors) == len(get_requests_with_400_status_code(self.path_to_log))

    def test_server_error(self):
        server_error = self.get_server_error()
        assert len(server_error) == len(get_requests_with_500_status_code(self.path_to_log))

