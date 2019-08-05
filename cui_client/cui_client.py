from cui_client.network import network_check


host_url = "http://localhost:16000/procon30-battle-api"


def exec_command(command):
    global host_url

    # Check
    if command[0] == "check":
        if len(command) == 1:
            print("Usage : check [connection]")
            return

        if command[1] == "connection":
            network_check(host_url)
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

        if command[0] == "exit":
            print("Bye")
            break

        if len(command) > 0:
            exec_command(command)
        print()