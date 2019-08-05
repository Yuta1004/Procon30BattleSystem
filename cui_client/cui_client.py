from cui_client.network import network_check


host_url = "http://localhost:16000/procon30-battle-api"


def cui_client_main():
    # バージョン表示とか
    print()
    print("Procon30 Battlle Syatem CUI Client ver0.0.1")
    print("Welcome user")
    print()

    # 初期化処理
    network_check(host_url)