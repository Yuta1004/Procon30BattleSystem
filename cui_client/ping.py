import urllib3
import json


def ping(host_url, token):
    api_url = host_url + "/ping"
    header = {"Authorization": token}
    http_connecter = urllib3.PoolManager()
    result = http_connecter.request("GET", api_url, headers=header)

    if result.status == 200:
        print("token ok")
    else:
        print("invalid token")
