import urllib3


def network_check(host_url):
    print("Host URL:", host_url)
    print("Checking connection ... ", end="")

    http_connecter = urllib3.PoolManager()
    try:
        result = http_connecter.request("GET", host_url)
    except urllib3.exceptions.MaxRetryError:
        print("Failed ( Connnection Refused )")
        return

    if (result.status == 200) and (result.data.decode() == "#procon30 Battle API"):
        print("OK")
    else:
        print("Failed (", result.staut, ")")
