import urllib3
import json;
from cui_client.table_stdout import get_data_and_output, table_output


def show_battle(host_url):
    api_url = host_url + "/battle"
    get_data_and_output(api_url)


def show_battle_id(host_url, battle_id):
    api_url = host_url + "/battle/" + str(battle_id)
    get_data_and_output(api_url)
