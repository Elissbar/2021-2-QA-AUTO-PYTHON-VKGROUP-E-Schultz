import requests
from urllib.parse import urljoin
import json


class ApiClient:

    def __init__(self, host, cookies=None, agent=None):
        self.host = host
        self.agent = agent
        self.session = requests.Session()
        self.session.cookies.set('session', cookies['value'])
        self.session.headers.setdefault("User-Agent", self.agent)

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
        resp = self.session.get(urljoin(self.host, url), headers={"User-Agent": self.agent})
        return resp
