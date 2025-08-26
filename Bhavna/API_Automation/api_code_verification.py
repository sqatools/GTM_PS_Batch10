import requests


def get_api_automation():

    url = "https://gorest.co.in/public/v2/users"

    payload = {}
    headers = {
        'Authorization': 'Bearer ec9036fc83b22786931d9afb2ecbee9a98b9beea86432c00306d1c8f52d5622f'
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    print(response.text)
    print(response.status_code)


# get_api_automation()

'''
curl -i -H "Accept:application/json" -H "Content-Type:application/json" -H "Authorization: Bearer ACCESS-TOKEN" -XPOST "https://gorest.co.in/public/v2/users" -d '{"name":"Tenali Ramakrishna", "gender":"male", "email":"tenali.ramakrishna@15ce.com", "status":"active"}'
'''


def post_method_verification():
    import requests
    import json

    url = "https://gorest.co.in/public/v2/users"

    payload = json.dumps({
        "name": "Shivani Singh",
        "gender": "female",
        "email": "shivani.singh@gm.com",
        "status": "active"

    })
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ec9036fc83b22786931d9afb2ecbee9a98b9beea86432c00306d1c8f52d5622f'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.text)


# post_method_verification()

# def put_method_verification():

    '''
    curl -i -H "Accept:application/json" -H "Content-Type:application/json" -H "Authorization: Bearer ec9036fc83b22786931d9afb2ecbee9a98b9beea86432c00306d1c8f52d5622f" -XPATCH "https://gorest.co.in/public/v2/users/7440270" -d '{"name":"Allasani Peddana", "email":"allasani.peddana@15ce.com", "status":"active"}'
    :return:
    '''