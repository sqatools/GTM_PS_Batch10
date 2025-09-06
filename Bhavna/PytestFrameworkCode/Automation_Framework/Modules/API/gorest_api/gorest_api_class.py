
from ....Base.api_base import APIBase
from .gorest_api_data import *


class GoRestAPI(APIBase):
    def __init__(self):
        super().__init__()

    def get_all_user_info(self):
        url = f"{gorest_com_uri}/users"
        res, sta_code = self.get_method(url=url, headers=all_users_headers)
        return res, sta_code

    def create_new_user(self):
        url = f"{gorest_com_uri}/users"
        res, sta_code = self.post_method(url=url, headers=create_users_entry, payload=create_users_payload)
        return res, sta_code

    def update_user_info(self):
        url = f"{gorest_com_uri}/users"
        user_res, user_st_code = self.post_method(url=url, headers=create_users_entry,
                                                  payload=json.dumps(update_users_payload))
        user_id = user_res["id"]
        patch_url = f"{gorest_com_uri}/users/{user_id}"
        update_users_payload['status'] = 'active'
        res, st_code = self.patch_method(url=patch_url, headers=create_users_entry,
                                         payload=json.dumps(update_users_payload))
        return res, st_code

    def delete_user_and_verify(self):
        url = f"{gorest_com_uri}/users/"
        user_res, user_st_code = self.post_method(url=url, headers=create_users_entry, payload=delete_users_payload)
        user_id = user_res["id"]
        delete_url = f"{gorest_com_uri}/users/{user_id}"
        res, st_code = self.delete_method(url=delete_url, headers=create_users_entry)
        return res, st_code
