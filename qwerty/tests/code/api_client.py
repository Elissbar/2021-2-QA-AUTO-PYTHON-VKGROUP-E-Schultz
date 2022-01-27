import requests
from urllib.parse import urljoin
import json


class ApiClient:

    def __init__(self, host, username, passwd):
        self.host = host
        self.username = username
        self.passwd = passwd
        self.session = requests.Session()

    def get_resp(self):
        resp = self.session.get(url=self.host)
        print(resp.status_code)
        print(resp.cookies)
        print(resp.headers)

    def post_login(self):
        headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36"}
        login = '/login'
        data = {
            "username": self.username,
            "password": self.passwd,
            "submit": "Login"
        }
        resp = self.session.post(urljoin(self.host, login), headers=headers, data=data)
        print(resp.status_code)
        print(resp.cookies)
        print(resp.headers)
        # return resp

    def delete_user(self, username):
        url_delete = f'/api/del_user/{username}'
        resp = self.session.get(url=urljoin(self.host, url_delete))
        print(resp.status_code)
        print(resp.cookies)
        print(resp.headers)
        # return resp.status_code, resp.content

    def post_add_user(self, username, password, email):
        data = {
            "username": username,
            "password": password,
            "email": email
        }
        # resp = self.session.post(urljoin(self.host, '/api/add_user'), data=data)
        resp = self.session.get(urljoin(self.host, '/api/block_user/testtest'))
        print(resp.status_code)
        print(resp.cookies)
        print(resp.content)


client = ApiClient(host="http://0.0.0.0:8080", username="testtest1", passwd="qwerty2")
# client.get_resp()
# print('='*50)
client.post_login()
# print('='*50)
# client.post_add_user(username="testtest", password="qwerty1!", email="code@code.ru")
# client.post_login()
# client.delete_user(username="testtest1")
