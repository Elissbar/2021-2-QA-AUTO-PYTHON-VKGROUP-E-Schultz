import pytest
from mysql_orm.client import MysqlORMClient
import os


def pytest_configure(config):
    mysql_orm_client = MysqlORMClient(user='root', password='pass', db_name='TEST_SQL')
    if not hasattr(config, 'workerinput'):
        mysql_orm_client.recreate_db()
    mysql_orm_client.connect(db_created=True)
    if not hasattr(config, 'workerinput'):
        mysql_orm_client.create_count_of_requests()
        mysql_orm_client.create_top_requests()
        mysql_orm_client.create_frequent_requests()
        mysql_orm_client.create_client_error()
        mysql_orm_client.create_server_error()

    config.mysql_orm_client = mysql_orm_client


@pytest.fixture(scope='session')
def mysql_orm_client(request) -> MysqlORMClient:
    client = request.config.mysql_orm_client
    yield client
    client.connection.close()


@pytest.fixture(scope='session')
def nginx_log():
    return os.path.abspath(os.path.join(os.path.dirname(__file__), 'parse/access.log'))


