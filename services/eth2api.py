import requests
from urllib.parse import urljoin


class API:
    def __init__(self, apiUrl):
        self.__apiUrl = apiUrl

    def request(self, url_path):
        response = requests.get(urljoin(self.__apiUrl, url_path))

        return response.json()


class BeaconAPI(API):
    def genesis(self):
        return self.request('/eth/v1/beacon/genesis')

    def block_root(self, block_id):
        return self.request(f"/eth/v1/beacon/blocks/{block_id}/root")

    def state_finality_checkpoints(self, state_id):
        return self.request(f"/eth/v1/beacon/states/{state_id}/finality_checkpoints")

    def block(self, block_id):
        return self.request(f"/eth/v2/beacon/blocks/{block_id}")


class ConfigAPI(API):
    def spec(self):
        return self.request('/eth/v1/config/spec')

    def deposit_contract(self):
        return self.request('/eth/v1/config/deposit_contract')

    def fork_schedule(self):
        return self.request('/eth/v1/config/fork_schedule')


class NodeAPI(API):
    def syncing(self):
        return self.request('/eth/v1/node/syncing')

    def version(self):
        return self.request('/eth/v1/node/version')

    def peers(self):
        return self.request('/eth/v1/node/peers')

    def peer_count(self):
        return self.request('/eth/v1/node/peer_count')


class DebugAPI(API):
    def bacon_state(self, state_id):
        return self.request(f"/eth/v2/debug/beacon/states/${state_id}")


class ETH2API:
    def __init__(self, apiUrl):
        self.apiUrl = apiUrl
        self.beacon = BeaconAPI(self.apiUrl)
        self.config = ConfigAPI(self.apiUrl)
        self.node = NodeAPI(self.apiUrl)
        self.debug = DebugAPI(self.apiUrl)
