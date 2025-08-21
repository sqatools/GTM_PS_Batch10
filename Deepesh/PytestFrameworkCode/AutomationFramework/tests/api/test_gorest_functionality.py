import pytest
from modules.api.gorest_api.gorest_api_class import GoRestAPI


class TestGoRest:
    @pytest.fixture(autouse=True)
    def setup(self):
        self.gr = GoRestAPI()

    def test_get_all_user_info_and_verify(self):
        resp, st_code = self.gr.get_all_user_info()
        assert st_code == 200

    def test_create_new_user_and_verify(self):
        resp, st_code = self.gr.create_new_user()
        assert st_code == 201
        assert "id" in resp
