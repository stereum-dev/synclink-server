from http import client
import httpx
from urllib.parse import urljoin

from validators.content_type import ContentTypeSSZ


class API:
    def __init__(self, apiUrl):
        self.apiUrl = apiUrl
        self.client = httpx.AsyncClient(base_url=apiUrl)

    async def request(self, url_path):
        response = await self.client.get(url_path)

        return response.json()


class BeaconAPI(API):
    async def genesis(self):
        return await self.request('/eth/v1/beacon/genesis')

    async def block_root(self, block_id):
        return await self.request(f"/eth/v1/beacon/blocks/{block_id}/root")

    async def state_finality_checkpoints(self, state_id):
        return await self.request(f"/eth/v1/beacon/states/{state_id}/finality_checkpoints")

    async def block(self, block_id):
        return await self.request(f"/eth/v2/beacon/blocks/{block_id}")


class ConfigAPI(API):
    async def spec(self):
        return await self.request('/eth/v1/config/spec')

    async def deposit_contract(self):
        return await self.request('/eth/v1/config/deposit_contract')

    async def fork_schedule(self):
        return await self.request('/eth/v1/config/fork_schedule')


class NodeAPI(API):
    async def health(self):
        return await self.client.get('/eth/v1/node/health')

    async def syncing(self):
        return await self.request('/eth/v1/node/syncing')

    async def version(self):
        return await self.request('/eth/v1/node/version')

    async def peers(self):
        return await self.request('/eth/v1/node/peers')

    async def peer_count(self):
        return await self.request('/eth/v1/node/peer_count')


class DebugAPI(API):
    def bacon_state(self, state_id):
        with httpx.stream("GET", urljoin(self.apiUrl, f"/eth/v2/debug/beacon/states/{state_id}"), headers={'Accept': 'application/octet-stream'}) as r:
            for chunk in r.iter_bytes():
                yield chunk


class ETH2API:
    def __init__(self, apiUrl):
        self.apiUrl = apiUrl
        self.beacon = BeaconAPI(self.apiUrl)
        self.config = ConfigAPI(self.apiUrl)
        self.node = NodeAPI(self.apiUrl)
        self.debug = DebugAPI(self.apiUrl)
