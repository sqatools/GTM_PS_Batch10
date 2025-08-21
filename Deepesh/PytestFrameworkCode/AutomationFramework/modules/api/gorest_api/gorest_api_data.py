"""
command to install the package
pip install fake
"""
import json
from faker import Faker
fk = Faker()

# server : https://gorest.co.in/

gorest_com_uri = "https://gorest.co.in/public/v2"
token = "b9b3492b489c402fe0cd7e9299e6fc7b172ccf67407937d21904aaffba74802e"

# get all userinfo details
all_users_headers = {
        'Authorization': f'Bearer {token}'
    }

# create new user entry
create_users_headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer b9b3492b489c402fe0cd7e9299e6fc7b172ccf67407937d21904aaffba74802e',
    }

create_user_payload = json.dumps({
        "name": f"{fk.user_name()}",
        "gender": "male",
        "email": f"{fk.email()}",
        "status": "active"
    })


# Update user info
update_user_payload = {
        "name": f"{fk.user_name()}",
        "gender": "male",
        "email": f"{fk.email()}",
        "status": "inactive"
    }


# Delete user info
delete_user_payload = json.dumps({
        "name": f"{fk.user_name()}",
        "gender": "male",
        "email": f"{fk.email()}",
        "status": "active"
    })