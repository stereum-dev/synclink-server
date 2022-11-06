import asyncio

from loguru import logger

from config.config import config
from core.node import Node


class SynclinkServer():
    def __init__(self, eth_api_address: Node) -> None:
        self.node = Node(eth_api_address)

    async def start(self):
        logger.info('Checking sync and health status of the node...')

        is_ready = await self.node.is_ready()
        while not is_ready:
            logger.warning('Not is not ready yet...')
            is_ready = await self.node.is_ready()
            await asyncio.sleep(5)

        logger.success('Node health is ok and not syncing.')

        logger.info('Checking spec of the node...')

        spec = await self.node.get_spec()
        while not spec:
            logger.warning('Not is not ready yet...')
            spec = await self.node.get_spec()
            await asyncio.sleep(5)

        logger.success('Spec fetched successfully.')


server = SynclinkServer(config.eth_api_address)
