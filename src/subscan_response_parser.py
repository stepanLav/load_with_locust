import json


def parse_subscan_accounts_response(response):
    addresses_list = []
    parsed_response = json.loads(response)
    for element in parsed_response['data']['list']:
        addresses_list.append(element['address'])

    return addresses_list