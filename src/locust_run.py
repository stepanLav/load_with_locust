import json
import os
import time
import random

from locust import HttpUser, between, events, task
from locust.user.task import tag
from locust.user.wait_time import constant

from query_builder import history_changes_by_address, stake_changes_by_address, get_accounts_from_subscan
from subscan_response_parser import parse_subscan_accounts_response

class QuickstartUser(HttpUser):
    wait_time = constant(float(os.environ.get('WAIT_TIME', 1)))
    host = "https://api.subquery.network"
    path = "/sq/nova-wallet/nova-polkadot__bm92Y"
    headers = {"content-type": "application/json",
               "user-agent": "nova/1 CFNetwork/978.0.7 Darwin/20.6.0",
               }
    network = "polkadot"
    all_request_to_one = False
    address = "12xtAYsRUrmbniiWQqJtECiBQrMn8AypQcXhnQAc6RB6XkLW"

    @tag('stake_changes')
    @task
    def stake_changes(self):
        data = json.dumps(stake_changes_by_address(random.choice(self.addresess)))
        self.client.post(self.path, data=data, headers=self.headers, name='stake_changes')

    @tag('history_elements')
    @task
    def history_elements(self):
        data = json.dumps(history_changes_by_address(
            self.address if self.all_request_to_one else random.choice(self.addresess)
            ))
        self.client.post(self.path, data=data, headers=self.headers, name='history_elements')

    def on_start(self):
        data = json.dumps(get_accounts_from_subscan("", 100, random.randint(0, 10)))
        response = self.client.post(
            url='https://%s.webapi.subscan.io/api/v2/scan/accounts'%(self.network),
            data=data,
            headers=self.headers,
            name="setup_request"
            )
        self.addresess = parse_subscan_accounts_response(response.text)
