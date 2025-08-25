import requests

def get_api_verification():

    url="https://gorest.co.in/public/v2/users"
    header= {
        'Authorization': 'Bearer b9b3492b489c402fe0cd7e9299e6fc7b172ccf67407937d21904aaffba74802e',
        'Cookie': '_gorest_session=wQkIuQ5O50U2eAXOS5hSkRJdToEz02Yj0abtAUvdxIAlvMdliVKuIEThaZYXvv7XHyKyOW0uH26KO1UFPVDFk1VgeK2%2B9SeyxoLkib0%2FiE%2FDNsOzTj6AV0pUW7Moky%2B5jGeduc%2FhGTZNu6MMSqq1CXO%2BX3Uc%2Bp3E8Ws1exA1xzzR%2BisxWLObmGZ1zIbKeuUK7JO2m3l%2BuWJmzlydeGwhHX6eSVPd1gM3sxwKwrbXVBTporQpCv2N54Hm7L8y%2BA9wA%2FDy7sAs5H3v5Df9PbWZVuQhZZiXxZQ%3D--PTHWSw7lDTJkIQ%2Bz--TLt30MNfj4swE%2BRS8mxVxw%3D%3D'
    }

    payload={}

    response=requests.request("GET",url, headers=header,data=payload)

    print(response.text)
    print(response.status_code)

get_api_verification()


