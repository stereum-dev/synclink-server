import uvicorn
from fastapi import FastAPI

from config.config import read
from routes.eth import eth_router

app = FastAPI()

app.include_router(eth_router, prefix='/eth')

if __name__ == "__main__":
    config = read('config.yaml')

    uvicorn.run("main:app", host="0.0.0.0", port=config['port'], reload=True)
