import requests
# pip install requests

def get_api_automation():

    url = "https://gorest.co.in/public/v2/users"

    payload = {}
    headers = {
        'Authorization': 'Bearer b9b3492b489c402fe0cd7e9299e6fc7b172ccf67407937d21904aaffba74802e',
        'Cookie': '_gorest_session=wQkIuQ5O50U2eAXOS5hSkRJdToEz02Yj0abtAUvdxIAlvMdliVKuIEThaZYXvv7XHyKyOW0uH26KO1UFPVDFk1VgeK2%2B9SeyxoLkib0%2FiE%2FDNsOzTj6AV0pUW7Moky%2B5jGeduc%2FhGTZNu6MMSqq1CXO%2BX3Uc%2Bp3E8Ws1exA1xzzR%2BisxWLObmGZ1zIbKeuUK7JO2m3l%2BuWJmzlydeGwhHX6eSVPd1gM3sxwKwrbXVBTporQpCv2N54Hm7L8y%2BA9wA%2FDy7sAs5H3v5Df9PbWZVuQhZZiXxZQ%3D--PTHWSw7lDTJkIQ%2Bz--TLt30MNfj4swE%2BRS8mxVxw%3D%3D'
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    print(response.text)
    print(response.status_code)


#get_api_automation()
"""
curl -i -H "Accept:application/json" -H "Content-Type:application/json" -H "Authorization: Bearer b9b3492b489c402fe0cd7e9299e6fc7b172ccf67407937d21904aaffba74802e" -XPOST "https://gorest.co.in/public/v2/users" -d '{"name":"Tenali Ramakrishna", "gender":"male", "email":"tenali.ramakrishna@15ce.com", "status":"active"}'

"""
def post_method_verification():
    import requests
    import json

    url = "https://gorest.co.in/public/v2/users"

    payload = json.dumps({
        "name": "Hemant123",
        "gender": "male",
        "email": "Hemant.rahul123@15ce.com",
        "status": "active"
    })
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer b9b3492b489c402fe0cd7e9299e6fc7b172ccf67407937d21904aaffba74802e',
        'Cookie': '_gorest_session=IEYvoCCb7uPD95pIel901bpjkgSzD2N9MQd6KeOyO8V2mR5YBnM0cM79jCZ5KA1aXkuqvUI05o3Zaz%2FFJPpHqic1sI4i%2FVcTIFEUFHN247ww7T9GC8CNo2MaJonvsXaViVv5vpIG3q188bPgjaCM4xhGnBFOKrWDODtN4ZnNfnol27kd3P9232NU%2Fl8qSjA5vCFb6JoEjA%2BPIt0%2BR3RbdjHBuvZmFfK6lyYSUxbWS1SEol%2BXk%2B4oEMgQLxsQS4XhxN4vzOADWF4BGxwBTUwlKObmdJie%2B78%3D--kylrZt556K0crzxd--IW0DslgSU%2Fg0zPdFSZM5cQ%3D%3D'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.text, response.status_code)

post_method_verification()