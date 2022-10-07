import uvicorn
from fastapi import BackgroundTasks, FastAPI
from fastapi.responses import StreamingResponse
import httpx


from config.config import read
from routes.eth import eth_router

client = httpx.AsyncClient()


app = FastAPI()

app.include_router(eth_router, prefix='/eth')


@app.get('/main')
async def get_main():
    r = await client.get('http://httpbin.org/uuid')
    return r.json()


if __name__ == "__main__":
    config = read('config.yaml')

    uvicorn.run("main:app", host="0.0.0.0", port=config['port'], reload=True)
