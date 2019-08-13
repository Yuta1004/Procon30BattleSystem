from cui_client.network import network_check, network_check_non_display
from cui_client.show_battle import show_battle, show_battle_id
from cui_client.show_team import show_team, show_team_id, show_team_token
from cui_client.ping import ping
from cui_client.register import register_battle, register_team
from cui_client.help import show_help
from cui_client.manage_battle import start_battle, finish_battle


host_url = "http://localhost:16000/procon30-battle-api"


def exec_command(command):
    global host_url

    # Help
    if command[0] == "help":
        show_help()
        return

    # Status
    if command[0] == "status":
        print("Host URL :", host_url)
        return

    # Set
    if command[0] == "set":
        if len(command) == 1:
            print("Usage : set [host]")
            return

        if command[1] == "host":
            print("input new host : ", end="")
            new_host = input()
            print("update ok? (", new_host, ") y/N : ", end="")
            res = input()
            if res == "y" or res == "Y":
                host_url = new_host
                print("update successed!")
            return

        print("Usage : set [host]")
        return

    # Network Connecton Check
    successed, _ = network_check_non_display(host_url)
    if not successed:
        print("Connection Error")
        return

    # Check
    if command[0] == "check":
        if len(command) == 1:
            print("Usage : check [connection/token]")
            return

        if command[1] == "connection":
            network_check(host_url)
            return

        if command[1] == "token":
            if len(command) == 3:
                ping(host_url, command[2])
            else:
                print("Usage : check token {token}")
            return

        print("Usage : check [connection]")
        return

    # Show
    if command[0] == "show":
        if len(command) == 1:
            print("Usage : show [battle/team]")
            return

        if command[1] == "battle":
            if len(command) == 2:
                show_battle(host_url)
            else:
                show_battle_id(host_url, command[2])
            return

        if command[1] == "team":
            if len(command) == 2:
                show_team(host_url)
            elif command[2] == "id":
                if len(command) == 3:
                    print("Usage : show team id {team_id}")
                else:
                    show_team_id(host_url, command[3])
            elif command[2] == "token":
                if len(command) == 3:
                    print("Usage : show team token {team_id}")
                else:
                    show_team_token(host_url, command[3])
            return

        print("Usage : show [battle/team]")
        return

    # Register
    if command[0] == "register":
        if len(command) == 1:
            print("Usage : register [battle/team]")
            return

        if command[1] == "battle":
            register_battle(host_url)
            return

        if command[1] == "team":
            register_team(host_url)
            return

        print("Usage : register [battle/team]")
        return

    # start
    if command[0] == "start":
        if len(command) == 1:
            print("Usage : start {battle_id}")
            return

        start_battle(host_url, command[1])
        return

    # finish
    if command[0] == "finish":
        if len(command) == 1:
            print("Usage : finish {battle_id}")
            return

        finish_battle(host_url, command[1])
        return

    # Not Found
    print("Command not found :", command[0])


def cui_client_main():
    # バージョン表示とか
    print()
    print("Procon30 Battlle Syatem CUI Client ver0.0.1")
    print("Welcome user")
    print()

    # 初期化処理
    network_check(host_url)
    print()

    # メインループ
    while True:
        print(">> ", end="")
        command = input().split()

        if len(command) == 0:
            continue
        elif command[0] == "exit":
            print("Bye")
            break

        if len(command) > 0:
            exec_command(command)
        print()