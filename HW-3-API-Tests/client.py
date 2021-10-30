import requests
import re


class ApiClient:

    cookies_list = []

    def __init__(self):
        self.session = requests.Session()
        self.csrf_token = None

    @staticmethod
    def find_cookies(all_cookies, cookies_names):
        pattern = r'Cookie (\w+)=(\w+)'
        find_all = re.findall(pattern, str(all_cookies))
        return [{'name': i[0], 'value': i[1]} for i in find_all if i[0] in cookies_names]

    def login(self, login, password):
        location = 'https://auth-ac.my.com/auth?lang=en&nosavelogin=0'
        headers = {'Referer': 'https://target.my.com/'}
        data = {
            'email': login,
            'password': password,
            'continue': 'https://target.my.com/auth/mycom?state=target_login%3D1%26ignore_opener%3D1#email'
        }
        self.session.post(location, headers=headers, data=data)
        self.session.get('https://target.my.com/csrf/')
        self.csrf_token = self.find_cookies(str(self.session.cookies), 'csrftoken')[0]['value']
        cookies_names = ['mc', 'sdc']
        new_cookies_list = self.find_cookies(self.session.cookies, cookies_names)
        return new_cookies_list

    def create_campaign(self, file_path, campaign_name):
        location = 'https://target.my.com/api/v2/content/static.json'
        files = {
            'file': open(file_path, 'rb'),
            "width": 240,
            "height": 400
        }
        headers = {
            'X-CSRFToken': self.csrf_token
        }
        result = self.session.post(location, headers=headers, files=files)
        image_id = result.json()['id']
        headers = {
            'X-CSRFToken': self.csrf_token
        }
        payload = {
            "name": f"{campaign_name}",
            "status": "active",
            # "date_start": None,
            # "date_end": None,
            # "budget_limit_day": None,
            # "budget_limit": None,
            # "conversion_funnel_id": None,
            # "age_restrictions": None,
            # "utm": None,
            "autobidding_mode": "second_price_mean",
            "enable_offline_goals": False,
            "mixing": "fastest",
            "price": "4.05",
            "enable_utm": True,
            "max_price": "0",
            "package_id": 961,
            "objective": "traffic",
            "read_only": False,
            "banners": [
            {
                "content": {"image_240x400": {"id": f"{image_id}"}},
                "urls": {"primary": {"id": 55401133}},
                "textblocks": {},
                "name": ""
            }],
            "targetings": {
                "age": {
                    "age_list": [0, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]
                },
                "fulltime": {
                    "flags": ["use_holidays_moving", "cross_timezone"],
                    "mon": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23],
                    "tue": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23],
                    "wed": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23],
                    "thu": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23],
                    "fri": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23],
                    "sat": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23],
                    "sun": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23],
                },
                "geo": {"regions": [188]},
                "pads": [102643],
                "sex": ["male", "female"],
                "interests": [],
                "interests_soc_dem": [],
                "mobile_operators": [],
                "mobile_types": ["tablets", "smartphones"],
                "mobile_vendors": [],
                "segments": [],
                "split_audience": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
            }
        }
        result = self.session.post('https://target.my.com/api/v2/campaigns.json', headers=headers, json=payload)
        return result.json()['id']

    def check_campaign(self, campaign_id):
        headers = {
            'X-CSRFToken': self.csrf_token
        }
        location = 'https://target.my.com/api/v2/campaigns.json?_status=active'
        resp = self.session.get(location, headers=headers)
        campaigns = resp.json()['items']
        campaign = [campaign for campaign in campaigns if campaign_id == campaign['id']]
        return len(campaign) != 0

    def delete_campaign(self, campaign_id):
        location = f'https://target.my.com/api/v2/campaigns/{campaign_id}.json'
        headers = {
            'X-CSRFToken': self.csrf_token
        }
        self.session.delete(location, headers=headers)

    def create_segment(self, segment_name):
        location = 'https://target.my.com/api/v2/remarketing/segments.json'
        headers = {
            'X-CSRFToken': self.csrf_token
        }
        payload = {
            "logicType": "or",
            "name": f"{segment_name}",
            "pass_condition": 1,
            "relations": [
                {
                    "object_type": "remarketing_player",
                    "params": {
                        "type": "positive",
                        "left": 365,
                        "right": 0
                    }
                }
            ]
        }
        resp = self.session.post(location, headers=headers, json=payload)
        return resp.json()['id']

    def check_segment(self, id_segment):
        location = f'https://target.my.com/api/v2/remarketing/segments.json'
        headers = {
            'X-CSRFToken': self.csrf_token
        }
        resp = self.session.get(location, headers=headers)
        segments = resp.json()['items']
        segment = [segment for segment in segments if id_segment == segment['id']]
        return len(segment) != 0

    def delete_segment(self, id_segment):
        location = f'https://target.my.com/api/v2/remarketing/segments/{id_segment}.json'
        headers = {
            'X-CSRFToken': self.csrf_token
        }
        self.session.delete(location, headers=headers)


