import asyncio

import pytest

from services.eth2api import ETH2API

api = ETH2API('http://135.181.33.84:5051')


@pytest.mark.asyncio
async def test_beacon_genesis():
    genesis = await api.beacon.genesis()

    assert genesis.data.genesis_time != None


@pytest.mark.asyncio
async def test_beacon_block_root():
    block_root = await api.beacon.block_root(block_id=0)

    assert block_root.data.root != None


@pytest.mark.asyncio
async def test_beacon_state_finality_checkpoints():
    finality = await api.beacon.state_finality_checkpoints(state_id='head')

    assert finality.data.current_justified.epoch


@pytest.mark.asyncio
async def test_beacon_block():
    block_id = '0'

    block = await api.beacon.block(block_id=0)

    assert block.data.message.slot == block_id


@pytest.mark.asyncio
async def test_config_spec():
    spec = await api.config.spec()

    assert spec.data.SLOTS_PER_EPOCH


@pytest.mark.asyncio
async def test_config_deposit_contract():
    deposit_contract = await api.config.deposit_contract()

    assert deposit_contract.data.address


@pytest.mark.asyncio
async def test_config_fork_schedule():
    fork_schedule = await api.config.fork_schedule()

    assert len(fork_schedule.data)


@pytest.mark.asyncio
async def test_node_health():
    health = await api.node.health()

    assert health


@pytest.mark.asyncio
async def test_node_syncing():
    syncing = await api.node.syncing()

    assert type(syncing.data.is_syncing) == bool


@pytest.mark.asyncio
async def test_node_version():
    version = await api.node.version()

    assert version.data.version


@pytest.mark.asyncio
async def test_node_peers():
    peers = await api.node.peers()

    assert len(peers.data)


@pytest.mark.asyncio
async def test_node_peer_count():
    peer_count = await api.node.peer_count()

    assert peer_count.data.connected


@pytest.fixture(scope="session")
def event_loop(request):
    loop = asyncio.get_event_loop()
    yield loop
    loop.close()
