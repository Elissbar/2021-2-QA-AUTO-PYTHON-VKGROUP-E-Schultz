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

    def post_add_user(self, username, password, email):
        url = '/api/add_user'
        data = {
            "username": username,
            "password": password,
            "email": email,
        }
        print(self.session.cookies)
        resp = self.session.post(urljoin(self.host, url), data=data)
        return resp
        # POST http://<APP_HOST>:<APP_PORT>/api/add_user
        # Content-Type: application/json
        # Body:
        # {
        #    "username": "<username>",
        #    "password": "<password>",
        #    "email": "<email>"
        # }
