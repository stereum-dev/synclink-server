import httpx
from services.eth2api import ETH2API

from core.config import Config, DepositContract


class Node():
    def __init__(self, url) -> None:
        self.client = httpx.AsyncClient(base_url=url)
        self.api = ETH2API(url)
        self.config = Config()

    async def is_cheackpointz_healthy(self) -> bool:
        return await self.client.get(url="/eth/v2/debug/beacon/states/finalized", timeout=2, headers={
            'Content-Type': 'application/json',
            'Accept': 'application/octet-stream'
        })

    async def is_working(self) -> bool:
        try:
            r = await self.api.node.version()
            if r.data.version.lower().startswith("checkpointz/"):
                r = await self.is_cheackpointz_healthy()
            else:
                r = await self.api.node.health()
            r.raise_for_status()

            return True
        except:
            return False

    async def is_syncing(self) -> bool:
        r = await self.api.node.syncing()

        return bool(r.data.is_syncing)

    async def is_ready(self) -> bool:
        working = await self.is_working()
        syncing = await self.is_syncing()

        return bool(working and not syncing)

    async def get_spec(self) -> bool:
        spec = await self.api.config.spec()
        fork_epochs = await self.api.config.fork_schedule()

        self.config = Config(spec=spec.data,
                             fork_epochs=fork_epochs.data,
                             deposit_contract=DepositContract(
                                 address=spec.data.DEPOSIT_CONTRACT_ADDRESS,
                                 chain_id=spec.data.DEPOSIT_CHAIN_ID))

        return self.config
