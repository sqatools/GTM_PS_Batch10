import pytest
from .database_entries import *

class Testparametrization:

    @pytest.mark.parametrize("username,password",[('user1','admin1'),('user2','admin2'),('user3','admin3'),('user4','admin4'),('user5','admin5'),('user6','admin6')])

    def test_login(self,username,password):
        if (username,password) in database_credentials:
            print("Login Successful")
        else:
            assert False, "Login Unsuccessful"