from fastapi import FastAPI
from loguru import logger
import uvicorn

from config.config import read
from routes.eth import eth_router
from routes.synclink import synclink_router
import core.synclink

app = FastAPI(
    title="SyncLink Server API",
    description="Specification of the SyncLink Server API",
    version="0.1.0",
)

app.include_router(synclink_router, prefix='/synclink')
app.include_router(eth_router, prefix='/eth')


@app.on_event("startup")
async def startup_event():
    await core.synclink.server.start()


if __name__ == "__main__":
    config = read('config.yaml')

    docs_addr = config.addr if config.addr != "0.0.0.0" else "127.0.0.1"
    docs_port = config.port

    logger.info(
        f"Server starting, find API docs at http://{docs_addr}:{docs_port}/docs")

    uvicorn.run("main:app", host=config.addr,
                port=config.port, reload=True)
