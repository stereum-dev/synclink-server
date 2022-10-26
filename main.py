from fastapi import FastAPI
from loguru import logger
from uvicorn import Config, Server

from config.config import read
from config.logger import setup_logging
from routes.eth import eth_router

app = FastAPI(
    title="SyncLink Server API",
    description="Specification of the SyncLink Server API",
    version="0.1.0",
)

app.include_router(eth_router, prefix='/eth')


if __name__ == "__main__":
    config = read('config.yaml')

    server = Server(Config("main:app", host=config['addr'],
                           port=config['port'], reload=True))

    setup_logging()

    server.run()

    docs_addr = config['addr'] if config['addr'] != "0.0.0.0" else "127.0.0.1"
    docs_port = config['port']

    logger.info(
        f"Server starting, find API docs at http://{docs_addr}:{docs_port}/docs")
