import uvicorn
from fastapi import BackgroundTasks, FastAPI
from fastapi.responses import StreamingResponse
import httpx


from config.config import read
from routes.eth import eth_router

client = httpx.AsyncClient()


app = FastAPI(
    title="SyncLink Server API",
    description="Specification of the SyncLink Server API",
    version="0.1.0",
)

app.include_router(eth_router, prefix='/eth')


if __name__ == "__main__":
    config = read('config.yaml')

    docs_addr = config['addr'] if config['addr'] != "0.0.0.0" else "127.0.0.1"
    docs_port = config['port']
    docs_line = '=' * 75
    print(docs_line);
    print(f"Server starting, find API docs at http://{docs_addr}:{docs_port}/docs")
    print(docs_line);
    
    uvicorn.run("main:app", host=config['addr'], port=config['port'], reload=True)
