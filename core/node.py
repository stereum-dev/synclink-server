from xmlrpc.client import Boolean

from models.get_spec_response import GetSpecResponseData
from services.eth2api import ETH2API

from core.spec import Spec


class Node():
    def __init__(self, url) -> None:
        self.api = ETH2API(url)
        self.spec = GetSpecResponseData()

    async def is_working(self) -> bool:
        try:
            r = await self.api.node.health()
            r.raise_for_status()

            return True
        except:
            return False

    async def is_syncing(self) -> bool:
        r = await self.api.node.syncing()

        return Boolean(r.data.is_syncing)

    async def is_ready(self) -> bool:
        working = await self.is_working()
        syncing = await self.is_syncing()

        return Boolean(working and not syncing)

    async def get_spec(self) -> bool:
        spec = await self.api.config.spec()

        self.spec = Spec(**spec.data.__dict__)

        return self.spec
