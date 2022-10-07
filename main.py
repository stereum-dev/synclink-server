import uvicorn
from fastapi import BackgroundTasks, FastAPI
from fastapi.responses import StreamingResponse
import httpx


from config.config import read
from routes.eth import eth_router

client = httpx.AsyncClient()


app = FastAPI()

app.include_router(eth_router, prefix='/eth')


if __name__ == "__main__":
    config = read('config.yaml')
    
    uvicorn.run("main:app", host=config['addr'], port=config['port'], reload=True)
