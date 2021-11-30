from urllib.parse import urljoin
from payloads.create_campaign import Payloads
import requests
import re


class ApiClient:

    def __init__(self, base_url):
        self.base_url = base_url
        self.session = requests.Session()
        self.csrf_token = None
        self.payloads = Payloads()

    @staticmethod
    def find_cookies(all_cookies, cookies_names):
        pattern = r'Cookie (\w+)=(\w+)'
        find_all = re.findall(pattern, str(all_cookies))
        return [{'name': i[0], 'value': i[1]} for i in find_all if i[0] in cookies_names]

    def post_login(self, login, password):
        location = 'https://auth-ac.my.com/auth?lang=en&nosavelogin=0'
        headers = {'Referer': self.base_url}
        data = {
            'email': login,
            'password': password,
            'continue': urljoin(self.base_url, 'auth/mycom?state=target_login%3D1%26ignore_opener%3D1#email'),
            'failure': 'https://account.my.com/login/?continue=https%3A%2F%2Faccount.my.com'
        }
        self.session.post(location, headers=headers, data=data)
        self.session.get(urljoin(self.base_url, 'csrf/'))
        self.csrf_token = self.find_cookies(str(self.session.cookies), 'csrftoken')[0]['value']
        # cookies_names = ['mc', 'sdc']

    def post_upload_file(self, file_path):
        location = 'api/v2/content/static.json'
        files = {
            'file': open(file_path, 'rb'),
            "width": 240,
            "height": 400
        }
        headers = {
            'X-CSRFToken': self.csrf_token
        }
        result = self.session.post(urljoin(self.base_url, location), headers=headers, files=files)
        image_id = result.json()['id']
        return image_id

    def get_check_campaign(self, campaign_id):
        location = 'api/v2/campaigns.json?_status=active'
        headers = {
            'X-CSRFToken': self.csrf_token
        }
        resp = self.session.get(urljoin(self.base_url, location), headers=headers)
        campaigns = resp.json()['items']
        campaign = [campaign for campaign in campaigns if campaign_id == campaign['id']]
        return len(campaign) != 0

    def post_create_segment(self, segment_name):
        location = 'api/v2/remarketing/segments.json'
        headers = {
            'X-CSRFToken': self.csrf_token
        }
        payload = self.payloads.segment_payload(segment_name=segment_name)
        resp = self.session.post(urljoin(self.base_url, location), headers=headers, json=payload)
        return resp.json()['id']

    def get_check_segment(self, id_segment):
        location = 'api/v2/remarketing/segments.json'
        headers = {
            'X-CSRFToken': self.csrf_token
        }
        resp = self.session.get(urljoin(self.base_url, location), headers=headers)
        segments = resp.json()['items']
        segment = [segment for segment in segments if id_segment == segment['id']]
        return len(segment) != 0

    def delete_delete_segment(self, id_segment):
        location = f'api/v2/remarketing/segments/{id_segment}.json'
        headers = {
            'X-CSRFToken': self.csrf_token
        }
        return self.session.delete(urljoin(self.base_url, location), headers=headers)


