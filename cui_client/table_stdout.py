from tabulate import tabulate


def table_output(table_items_json):
    # 出力
    if len(table_items_json) == 0:
        return
    headers = list(table_items_json[0].keys())
    table = []
    for row in table_items_json:
        table.append(list(row.values()))
    print(tabulate(table, headers, tablefmt="grid"))
