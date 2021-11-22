from models.model import *
from parse.parse_logs import *


class MysqlORMBuilder:

    def __init__(self, client):
        self.client = client

    def create_count_of_requests(self, path):
        count_requests = CountOfRequests(
            count=return_count_requests(path)
        )
        self.client.session.add(count_requests)
        self.client.session.commit()
        return count_requests

    def create_top_requests(self, type, count):
        top_requests = TopRequests(
            type=type,
            count=count
        )
        self.client.session.add(top_requests)
        self.client.session.commit()
        return top_requests

    def create_frequent_requests(self, url, count):
        frequent_requests = FrequentRequests(
            url=url,
            count=count
        )
        self.client.session.add(frequent_requests)
        self.client.session.commit()
        return frequent_requests

    def create_client_errors(self, url, code, value, ip):
        client_errors = ClientError(
            url=url,
            code=code,
            value=value,
            ip=ip
        )
        self.client.session.add(client_errors)
        self.client.session.commit()
        return client_errors

    def create_server_error(self, ip, count):
        server_errors = ServerError(
            ip=ip,
            count=count
        )
        self.client.session.add(server_errors)
        self.client.session.commit()
        return server_errors


