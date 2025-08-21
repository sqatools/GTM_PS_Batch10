from base.api_base import APIBase
from .gorest_api_data import *


class GoRestAPI(APIBase):
    def __init__(self):
        super().__init__()

    def get_all_user_info(self):
        url = f"{gorest_com_uri}/users"
        res, st_code = self.get_method(url=url, headers=all_users_headers)
        return res, st_code

    def create_new_user(self):
        url = f"{gorest_com_uri}/users"
        res, st_code = self.post_method(url=url, headers=create_users_headers, payload=create_user_payload)
        return res, st_code





