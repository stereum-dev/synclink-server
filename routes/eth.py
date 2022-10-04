
from config.config import read
from fastapi import APIRouter, Header
from services.eth2api import ETH2API
from validators.content_type import (ContentTypeJSON, validate_content_type)


config = read(file_name='config.yaml')
api = ETH2API(config['eth_api_address'])


eth_router = APIRouter()


@eth_router.get("/v1/beacon/genesis", tags=["Beacon"])
async def handle_eth_v1_beacon_genesis(content_type: str = Header(default=ContentTypeJSON)):
    validate_content_type(content_type, ContentTypeJSON)

    r = api.beacon.genesis()

    return r


@eth_router.get("/v1/beacon/blocks/{block_id}/root", tags=["Beacon"])
async def handle_eth_v1_beacon_blocks_root(block_id, content_type: str = Header(default=ContentTypeJSON)):
    validate_content_type(content_type, ContentTypeJSON)

    r = api.beacon.block_root(block_id)

    return r


@eth_router.get("/v1/beacon/states/{state_id}/finality_checkpoints", tags=["Beacon"])
async def handle_eth_v1_beacon_blocks_root(state_id, content_type: str = Header(default=ContentTypeJSON)):
    validate_content_type(content_type, ContentTypeJSON)

    r = api.beacon.state_finality_checkpoints(state_id)

    return r


@eth_router.get("/v1/config/spec", tags=["Config"])
async def handle_eth_v1_config_spec(content_type: str = Header(default=ContentTypeJSON)):
    validate_content_type(content_type, ContentTypeJSON)

    r = api.config.spec()

    return r


@eth_router.get("/v1/config/deposit_contract", tags=["Config"])
async def handle_eth_v1_config_deposit_contract(content_type: str = Header(default=ContentTypeJSON)):
    validate_content_type(content_type, ContentTypeJSON)

    r = api.config.deposit_contract()

    return r


@eth_router.get("/v1/config/fork_schedule", tags=["Config"])
async def handle_eth_v1_config_fork_schedule(content_type: str = Header(default=ContentTypeJSON)):
    validate_content_type(content_type, ContentTypeJSON)

    r = api.config.fork_schedule()

    return r


@eth_router.get("/v1/node/syncing", tags=["Node"])
async def handle_eth_v1_config_fork_schedule(content_type: str = Header(default=ContentTypeJSON)):
    validate_content_type(content_type, ContentTypeJSON)

    r = api.node.syncing()

    return r


@eth_router.get("/v1/node/version", tags=["Node"])
async def handle_eth_v1_config_fork_schedule(content_type: str = Header(default=ContentTypeJSON)):
    validate_content_type(content_type, ContentTypeJSON)

    r = api.node.version()

    return r


@eth_router.get("/v1/node/peers", tags=["Node"])
async def handle_eth_v1_config_fork_schedule(content_type: str = Header(default=ContentTypeJSON)):
    validate_content_type(content_type, ContentTypeJSON)

    r = api.node.peers()

    return r


@eth_router.get("/v1/node/peer_count", tags=["Node"])
async def handle_eth_v1_config_fork_schedule(content_type: str = Header(default=ContentTypeJSON)):
    validate_content_type(content_type, ContentTypeJSON)

    r = api.node.peer_count()

    return r
