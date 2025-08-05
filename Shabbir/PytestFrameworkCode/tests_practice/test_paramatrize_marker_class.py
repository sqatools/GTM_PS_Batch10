import pytest
from database_entries import  *

class TestParametrization:

    @pytest.mark.parametrize("username, password", [
        ('user1', 'admin123'), ('user2', 'admin@145'), ('user3', 'admin876'),
        ('user4', 'user123'), ('user5', 'root@123'), ('user6', 'rootvalue123')

    ])
    def test_login(self, username, password):
        if (username, password) in database_creds:
            print("login Successful")
        else:
            assert False, "Login Failed, in valid credentials"

