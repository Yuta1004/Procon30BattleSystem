import urllib3
import json;
from cui_client.table_stdout import table_output


def show_battle(host_url):
    api_url = host_url + "/battle"
    http_connecter = urllib3.PoolManager()
    result = http_connecter.request("GET", api_url)

    if result.status == 200:
        result_json = json.loads(result.data.decode())
        table_output(result_json)
    else:
        print("no data")


def show_battle_id(host_url, battle_id):
    api_url = host_url + "/battle/" + str(battle_id)
    http_connecter = urllib3.PoolManager()
    result = http_connecter.request("GET", api_url)

    if result.status == 200:
        result_json = json.loads(result.data.decode())
        table_output([result_json])
    else:
        print("no data")
