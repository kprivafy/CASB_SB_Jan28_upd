import requests
import time
import json
import base64


def add_user(headers,payload):
        print("")
        print("add user ")
        url= "https://dashboard.lp.parsecs307.com/api/v1/accounts/pranav.srivastava+veea02@privafy.com/users"
        print("url : "+url)

        print(payload)
        response = requests.request('POST', url, headers = headers, json = payload, verify=False,timeout=200)
        time.sleep(5)
        print(response.status_code)
        print(response.text)
