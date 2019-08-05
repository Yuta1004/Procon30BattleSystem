from cui_client.network import network_check
from cui_client.show_battle import show_battle, show_battle_id
from cui_client.ping import ping
from cui_client.register import register_battle
from cui_client.help import show_help


host_url = "http://localhost:16000/procon30-battle-api"


def exec_command(command):
    global host_url

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

    # Show
    if command[0] == "show":
        if len(command) == 1:
            print("Usage : show [battle] {battle_id}")
            return

        if command[1] == "battle":
            if len(command) == 2:
                show_battle(host_url)
            else:
                show_battle_id(host_url, command[2])
        return

    # Register
    if command[0] == "register":
        if len(command) == 1:
            print("Usage : register [battle/team]")
            return

        if command[1] == "battle":
            register_battle(host_url)
        return

    # Status
    if command[0] == "status":
        print("Host URL :", host_url)
        return

    # Help
    if command[0] == "help":
        show_help()
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