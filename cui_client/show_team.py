import urllib3
import json;
from cui_client.table_stdout import get_data_and_output, table_output


def show_team(host_url):
    api_url = host_url + "/team"
    get_data_and_output(api_url)


def show_team_id(host_url, team_id):
    api_url = host_url + "/team/id/" + str(team_id)
    get_data_and_output(api_url)


def show_team_token(host_url, token):
    api_url = host_url + "/team/token/" + str(token)
    get_data_and_output(api_url)
