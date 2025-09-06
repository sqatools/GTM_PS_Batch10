import json
from faker import Faker
fk = Faker()
gorest_com_uri = "https://gorest.co.in/public/v2"
token = "ec9036fc83b22786931d9afb2ecbee9a98b9beea86432c00306d1c8f52d5622f"

# get all userinfo details
all_users_headers = {
        'Authorization': f'Bearer {token}'
    }

# create new user entry
create_users_entry = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ec9036fc83b22786931d9afb2ecbee9a98b9beea86432c00306d1c8f52d5622f'
    }
create_users_payload = json.dumps({
        "name": f"{fk.user_name()}",
        "gender": "male",
        "email": f"{fk.email()}",
        "status": "active"

    })

# Update user info
update_users_payload = {
        "name": f"{fk.user_name()}",
        "gender": "male",
        "email": f"{fk.email()}",
        "status": "inactive"

    }

# delete user info

delete_users_payload = json.dumps({
        "name": f"{fk.user_name()}",
        "gender": "male",
        "email": f"{fk.email()}",
        "status": "active"

    })