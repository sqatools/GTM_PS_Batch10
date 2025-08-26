import requests
import logging


class APIBase:
    def __init__(self):
        self.log = logging.getLogger(__name__)

    def get_method(self, url, headers=None, payload=None):
        headers = {} if headers is None else headers
        payload = {} if payload is None else payload
        response = requests.request("GET", url, headers=headers, data=payload)
        self.log.info("Method Name : get_method")
        self.log.info(f"URL: {url}")
        self.log.info(f"Headers: {headers}")
        self.log.info(f"Payload: {payload}")
        self.log.info(f"response: {response.text}")
        self.log.info(f"status code: {response.status_code}")
        return response.json(), response.status_code

    def post_method(self, url, headers=None, payload=None):
        headers = {} if headers is None else headers
        payload = {} if payload is None else payload
        response = requests.request("POST", url, headers=headers, data=payload)
        self.log.info("Method Name : post_method")
        self.log.info(f"URL: {url}")
        self.log.info(f"Headers: {headers}")
        self.log.info(f"Payload: {payload}")
        self.log.info(f"response: {response.text}")
        self.log.info(f"status code: {response.status_code}")
        return response.json(), response.status_code

    def put_method(self, url, headers=None, payload=None):
        headers = {} if headers is None else headers
        payload = {} if payload is None else payload
        response = requests.request("PUT", url, headers=headers, data=payload)
        self.log.info("Method Name : put_method")
        self.log.info(f"URL: {url}")
        self.log.info(f"Headers: {headers}")
        self.log.info(f"Payload: {payload}")
        self.log.info(f"response: {response.text}")
        self.log.info(f"status code: {response.status_code}")
        return response.json(), response.status_code

    def patch_method(self, url, headers=None, payload=None):
        headers = {} if headers is None else headers
        payload = {} if payload is None else payload
        response = requests.request("PATCH", url, headers=headers, data=payload)
        self.log.info("Method Name : patch_method")
        self.log.info(f"URL: {url}")
        self.log.info(f"Headers: {headers}")
        self.log.info(f"Payload: {payload}")
        self.log.info(f"response: {response.text}")
        self.log.info(f"status code: {response.status_code}")
        return response.json(), response.status_code

    def delete_method(self, url, headers=None, payload=None):
        headers = {} if headers is None else headers
        payload = {} if payload is None else payload
        response = requests.request("DELETE", url, headers=headers, data=payload)
        self.log.info("Method Name : delete_method")
        self.log.info(f"URL: {url}")
        self.log.info(f"Headers: {headers}")
        self.log.info(f"Payload: {payload}")
        self.log.info(f"response: {response.text}, {type(response.text)}")
        self.log.info(f"status code: {response.status_code}")
        if response.text == "":
            return response, response.status_code
        else:
            return response.json(), response.status_code
