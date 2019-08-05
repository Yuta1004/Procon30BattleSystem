import urllib3
import json


def start_battle(host_url, battle_id):
    api_url = host_url + "/battle/start/" + str(battle_id)
    http_connecter = urllib3.PoolManager()
    result = http_connecter.request("GET", api_url)

    if result.status == 200:
        print("battle started! ( battle_id:", battle_id, "}")
        return
    else:
        response_json = json.loads(result.data.decode())
        print("error (", response_json["status"], ")")
