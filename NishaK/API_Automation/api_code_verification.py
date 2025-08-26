import requests


def get_api_automation():
    url = "https://gorest.co.in/public/v2/users"

    payload = {}
    headers = {
        'Authorization': 'Bearer bbde576904dc0e3f576fb2d432b00aa617c558dd8d1604f1330712565532cad0',
        'Cookie': '_gorest_session=kRBBPxnZlWn5qqI4YBhjBjjc8jw47v7Wm1ZIWrtteDA7WCrlpKRY0Q%2BffYEcJlZdOWpmER71LRBqIZQaqhoc%2FjefjyiJz%2B7SzqKGyOKxretYJv%2FHSuYPcmaH2iAp4zhrTkTflPswh4HPH4y1Nj1HD9BObUY4Fn2HlQwQHh4JRr71SX1hya4BbShnvxCGUHWIR6rWLMhhLCrO7CdMonbxtW2qGpUHlFySAFgnuzEsQMY%2F5BPui17PwYpFMH5aB4cBQSilWyqvp%2FhoMCfhvxPG8O1B4731egs%3D--RneZCryWcflZQWat--YGJLM9nWR%2FMks9caPmkZ9Q%3D%3D'
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    print(response.text)
    print(response.status_code)


# get_api_automation()

"""
curl -i -H "Accept:application/json" -H "Content-Type:application/json" -H "Authorization: Bearer ACCESS-TOKEN" -XPOST "https://gorest.co.in/public/v2/users" -d '{"name":"Tenali Ramakrishna", "gender":"male", "email":"tenali.ramakrishna@15ce.com", "status":"active"}'
"""


def post_method_verification():
    import requests
    import json

    url = "https://gorest.co.in/public/v2/users"

    payload = json.dumps({
        "name": "sham Ramakrishna",
        "gender": "male",
        "email": "sham.ramakrishna@15ce.com",
        "status": "active"
    })
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer bbde576904dc0e3f576fb2d432b00aa617c558dd8d1604f1330712565532cad0',
        'Cookie': '_gorest_session=HrGnIgE7Jhb5%2Fov2up5vwBFLnWt9ryigqCOYVdOdfE9RjvpT6RnCqynsT9zQ4jZRlxPtNpZh70KtaJ9wa5H5wKJx2It4rPP1AqXThmtslCSAwH%2BsvY%2FFJ2wLmN8IeOdfV%2BErKpC8tBQF2VsFX8eKPDu4cGWAmxvrphwmylJq9lPq8p%2F80pYHX%2FKFxrR1GI8a6htaG4WRi9xnint8DdecjUQ7ii1NVyu9xuaMB2aQ10T5TH51DxxL2xe4fyt3RLUCXCllyRJlWOUmNcSJEA5dIh6AbWCm%2BqI%3D--4H0ViNNXbotPHARS--tFd7BgXh4y1DE55DKfzTCA%3D%3D'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.text)
    print(response.status_code)


post_method_verification()
