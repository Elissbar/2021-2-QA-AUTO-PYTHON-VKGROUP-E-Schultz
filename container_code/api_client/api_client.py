import requests
import http.cookiejar as cookiejar
from urllib.parse import urljoin
import json


class ApiClient:

    def __init__(self, host, cookies=None, agent=None):
        self.host = host
        self.agent = agent
        self.session = requests.Session()
        self.session.cookies.set('session', cookies[0]['value'])
        # self.session.headers.setdefault("User-Agent", self.agent)

    def post_login(self, username, passwd):
        headers = {"User-Agent": self.agent}
        login = '/login'
        data = {
            "username": username,
            "password": passwd,
            "submit": "Login"
        }
        resp = self.session.post(urljoin(self.host, login), headers=headers, data=data)
        return resp

    def get_delete(self, username):
        url = f'/api/del_user/{username}'
        resp = self.session.get(urljoin(self.host, url))
        return resp

    def post_add_user(self, username, password, email):
        headers = {'Content-type': 'application/json'}
        data = {
            "username": username,
            "password": password,
            "email": email,
        }
        resp = self.session.post(f'{self.host}/api/add_user', headers=headers, data=json.dumps(data))
        return resp

    def get_block_user(self, username):
        url = f'/api/block_user/{username}'
        return self.session.get(urljoin(self.host, url))

    def get_unblock_user(self, username):
        url = f'/api/accept_user/{username}'
        return self.session.get(urljoin(self.host, url))

    def get_app_state(self):
        url = f'/status'
        return self.session.get(urljoin(self.host, url))

