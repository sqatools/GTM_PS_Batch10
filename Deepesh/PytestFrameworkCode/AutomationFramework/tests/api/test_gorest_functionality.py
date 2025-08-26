import pytest
from modules.api.gorest_api.gorest_api_class import GoRestAPI


class TestGoRest:
    @pytest.fixture(autouse=True)
    def setup(self):
        self.gr = GoRestAPI()

    def test_get_all_user_info_and_verify(self, request):
        self.gr.log.info(f"Test Name: {request.node.name}")
        resp, st_code = self.gr.get_all_user_info()
        assert st_code == 200

    def test_create_new_user_and_verify(self, request):
        self.gr.log.info(f"Test Name: {request.node.name}")
        resp, st_code = self.gr.create_new_user()
        assert st_code == 201
        assert "id" in resp

    def test_update_userinfo_and_verify(self, request):
        self.gr.log.info(f"Test Name: {request.node.name}")
        resp, st_code = self.gr.update_user_info()
        assert st_code == 200
        assert resp["status"] == "active"

    def test_delete_user_and_verify(self, request):
        self.gr.log.info(f"Test Name: {request.node.name}")
        resp, st_code = self.gr.delete_user_and_verify()
        assert st_code == 204
