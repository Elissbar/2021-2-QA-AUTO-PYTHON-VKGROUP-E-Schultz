class Payloads:

    def __init__(self):
        self.fulltime = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23]
        self.age_list = [0, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]
        self.split_audience = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    def campaign_payload(self, campaign_name, file_id):
        return {
            "name": f"{campaign_name}",
            "status": "active",
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
                "content": {"image_240x400": {"id": f"{file_id}"}},
                "urls": {"primary": {"id": 55401133}},
                "textblocks": {},
                "name": ""
            }],
            "targetings": {
                "age": {
                    "age_list": self.age_list
                },
                "fulltime": {
                    "flags": ["use_holidays_moving", "cross_timezone"],
                    "mon": self.fulltime,
                    "tue": self.fulltime,
                    "wed": self.fulltime,
                    "thu": self.fulltime,
                    "fri": self.fulltime,
                    "sat": self.fulltime,
                    "sun": self.fulltime,
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
                "split_audience": self.split_audience
            }
        }

    def segment_payload(self, segment_name):
        return {
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
