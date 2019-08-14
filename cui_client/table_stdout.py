import urllib3
import json;
from tabulate import tabulate


def get_data_and_output(api_url):
    http_connecter = urllib3.PoolManager()
    result = http_connecter.request("GET", api_url)

    if result.status == 200:
        result_json = json.loads(result.data.decode())
        if type(result_json) != list:
            result_json = [result_json]
        table_output(result_json)
    else:
        print("no data")


def table_output(table_items_json):
    # 出力
    if len(table_items_json) == 0:
        print("No data.")
        return
    headers = list(table_items_json[0].keys())
    table = []
    for row in table_items_json:
        table.append(list(row.values()))
    print(tabulate(table, headers, tablefmt="grid"))
