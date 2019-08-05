import urllib3
import json;
from tabulate import tabulate


def show_battle(host_url):
    api_url = host_url + "/battle"
    http_connecter = urllib3.PoolManager()
    result = http_connecter.request("GET", api_url)

    if result.status == 200:
        result_json = json.loads(result.data.decode())
        __battle_output(result_json)
    else:
        print("no data")


def show_battle_id(host_url, battle_id):
    api_url = host_url + "/battle/" + str(battle_id)
    http_connecter = urllib3.PoolManager()
    result = http_connecter.request("GET", api_url)

    if result.status == 200:
        result_json = json.loads(result.data.decode())
        __battle_output([result_json])
    else:
        print("no data")


def __battle_output(battle_list_json):
    # 出力
    if len(battle_list_json) == 0:
        return
    headers = list(battle_list_json[0].keys())
    table = []
    for battle in battle_list_json:
        table.append(list(battle.values()))
    print(tabulate(table, headers, tablefmt="grid"))
