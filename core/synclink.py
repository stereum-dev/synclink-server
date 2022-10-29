from config.config import read
from loguru import logger

from core.node import Node


class SynclinkServer():
    def __init__(self, eth_api_address: Node) -> None:
        self.node = Node(eth_api_address)

    async def start(self):
        await self.node.is_ready()
        logger.success('Node health is ok and not syncing.')

        await self.node.get_spec()
        logger.success('Spec fetched successfully.')


server = SynclinkServer(read('config.yaml').eth_api_address)
