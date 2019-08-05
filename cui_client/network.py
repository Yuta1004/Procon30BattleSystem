import urllib3


def network_check(host_url):
    print("Host URL:", host_url)
    print("Checking connection ... ", end="")

    successed, message = network_check_non_display(host_url)

    if successed:
        print("OK")
    else:
        print("Failed (", message, ")")


def network_check_non_display(host_url):
    http_connecter = urllib3.PoolManager()
    try:
        result = http_connecter.request("GET", host_url)
    except urllib3.exceptions.MaxRetryError:
        return False, "Connection refused!"

    if result.data.decode() == "#procon30 Battle API":
        return True, "ok"
    else:
        return False, "Unkown Error"

