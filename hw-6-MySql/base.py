import pytest
from mysql_orm.client import MysqlORMClient
from utils.builder_orm import MysqlORMBuilder
from models.model import *
from parse.parse_logs import *


class Base:

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, mysql_orm_client, file_to_log):
        self.mysql: MysqlORMClient = mysql_orm_client
        self.mysql_builder: MysqlORMBuilder = MysqlORMBuilder(self.mysql)
        self.path_to_log = file_to_log

    def get_count_requests(self):
        self.mysql_builder.create_count_of_requests(self.path_to_log)
        self.mysql.session.commit()
        count_requests = self.mysql.session.query(CountOfRequests)
        return count_requests.all()

    def get_top_requests(self):
        requests = count_requests_with_type(self.path_to_log)
        for request in requests:
            self.mysql_builder.create_top_requests(type=request[0], count=request[1])
        self.mysql.session.commit()
        top_requests = self.mysql.session.query(TopRequests)
        return top_requests.all()

    def get_frequent_url(self):
        urls = get_url(self.path_to_log)
        for url in urls:
            self.mysql_builder.create_frequent_requests(url=url[0], count=url[1])
        self.mysql.session.commit()
        frequent_requests = self.mysql.session.query(FrequentRequests)
        return frequent_requests.all()

    def get_client_errors(self):
        errors = get_requests_with_400_status_code(self.path_to_log)
        for error in errors:
            self.mysql_builder.create_client_errors(url=error[0], code=error[1], value=error[2], ip=error[3])
        self.mysql.session.commit()
        client_errors = self.mysql.session.query(ClientError)
        return client_errors.all()

    def get_server_error(self):
        errors = get_requests_with_500_status_code(self.path_to_log)
        for error in errors:
            self.mysql_builder.create_server_error(ip=error[0], count=error[1])
        self.mysql.session.commit()
        server_error = self.mysql.session.query(ServerError)
        return server_error.all()




