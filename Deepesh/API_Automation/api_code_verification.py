import requests
# pip install request

def get_api_automation():

    url = "https://gorest.co.in/public/v2/users"

    payload = {}
    headers = {
        'Authorization': 'Bearer 2fcabc17443f5e15070811c38f35b257838683a00fa76ef22471ebd4001ab7b5',
        'Cookie': '_gorest_session=wQkIuQ5O50U2eAXOS5hSkRJdToEz02Yj0abtAUvdxIAlvMdliVKuIEThaZYXvv7XHyKyOW0uH26KO1UFPVDFk1VgeK2%2B9SeyxoLkib0%2FiE%2FDNsOzTj6AV0pUW7Moky%2B5jGeduc%2FhGTZNu6MMSqq1CXO%2BX3Uc%2Bp3E8Ws1exA1xzzR%2BisxWLObmGZ1zIbKeuUK7JO2m3l%2BuWJmzlydeGwhHX6eSVPd1gM3sxwKwrbXVBTporQpCv2N54Hm7L8y%2BA9wA%2FDy7sAs5H3v5Df9PbWZVuQhZZiXxZQ%3D--PTHWSw7lDTJkIQ%2Bz--TLt30MNfj4swE%2BRS8mxVxw%3D%3D'
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    print(response.text)
    print(response.status_code)


get_api_automation()

def post_method_verification():
    pass