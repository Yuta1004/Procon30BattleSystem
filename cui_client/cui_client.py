from cui_client.network import network_check


host_url = "http://localhost:16000/procon30-battle-api"


def exec_command(command):
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