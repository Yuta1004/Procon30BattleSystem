import urllib3
import json
import time
from datetime import datetime


def register_battle(host_url):
    # 情報収集
    battle_info = {}
    request_list = [
        ["BattleName", str, "name"],
        ["StartDateTime (Y)", int, None],
        ["StartDateTime (M)", int, None],
        ["StartDateTime (D)", int, None],
        ["StartDateTime (h)", int, None],
        ["StartDateTime (m)", int, None],
        ["StartDateTime (s)", int, None],
        ["PlayerNum", int, "playerNum"],
        ["Turn", int, "turn"],
        ["TurnMillis (30000)", int, "turnMillis"],
        ["IntervalMillis (3000)", int, "intervalMillis"],
        ["BoardWidth", int, "width"],
        ["BoardHeight", int, "height"],
        ["PointLower", int, "pointLower"],
        ["PointUpper", int, "pointUpper"],
        ["TeamAID", int, "teamA"],
        ["TeamBID", int, "teamB"],
        ["GenerateBoardType (0)", int, "generateBoardType"]
    ]

    for request in request_list:
        print(request[0] + " : ", end="")
        res = ""
        while res == "": res = input()
        if request[1] == int:
            res = int(res)
        if request[2] is not None:
            battle_info[request[2]] = res
        else:
            battle_info[request[0]] = res

    # 日時表記 -> UNIX時間表記
    start_battle_time = datetime(
        battle_info["StartDateTime (Y)"],
        battle_info["StartDateTime (M)"],
        battle_info["StartDateTime (D)"],
        battle_info["StartDateTime (h)"],
        battle_info["StartDateTime (m)"],
        battle_info["StartDateTime (s)"]
    )
    start_at_unix_time = int(time.mktime(start_battle_time.timetuple()))
    battle_info["startAtUnixTime"] = start_at_unix_time
    del(battle_info["StartDateTime (Y)"])
    del(battle_info["StartDateTime (M)"])
    del(battle_info["StartDateTime (D)"])
    del(battle_info["StartDateTime (h)"])
    del(battle_info["StartDateTime (m)"])
    del(battle_info["StartDateTime (s)"])

    # 確認
    print()
    print("register ok? y/N : ", end="")
    res = ""
    while res == "": res = input()
    if not(res == "y" or res == "Y"):
        print("register finish")
        return

    # 通信
    api_url = host_url + "/battle/register"
    headers = {"Content-Type": "application/json"}
    http_connecter = urllib3.PoolManager()
    result = http_connecter.request(
        "POST", api_url, body=json.dumps(battle_info), headers=headers
    )

    if result.status == 200:
        response_json = json.loads(result.data.decode())
        print("register successed! ( BattleID:", response_json["battleID"], ")")
    else:
        print("error (", result.status, ")")


def register_team(host_url):
    # 情報収集
    battle_info = {}
    request_list = [
        ["TeamName", "name"],
        ["Token", "token"]
    ]

    for request in request_list:
        print(request[0] + " : ", end="")
        res = ""
        while res == "": res = input()
        battle_info[request[1]] = res

    # 確認
    print()
    print("register ok? y/N : ", end="")
    res = ""
    while res == "": res = input()
    if not(res == "y" or res == "Y"):
        print("register finish")
        return

    # 通信
    api_url = host_url + "/team/register"
    headers = {"Content-Type": "application/json"}
    http_connecter = urllib3.PoolManager()
    result = http_connecter.request(
        "POST", api_url, body=json.dumps(battle_info), headers=headers
    )

    if result.status == 200:
        print("register successed!")
    else:
        print("error (", result.status, ")")
