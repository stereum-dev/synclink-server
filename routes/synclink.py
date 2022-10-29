import core.synclink
from core.config import Config
from fastapi import APIRouter, Header
from validators.content_type import ContentTypeJSON, validate_content_type

synclink_router = APIRouter()

node = core.synclink.server.node


@synclink_router.get("/v1/config", tags=["Synclink"], response_model=Config)
async def handle_synclink_v1_config(content_type: str = Header(default=ContentTypeJSON)):
    validate_content_type(content_type, [ContentTypeJSON])

    return node.config
