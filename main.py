import uvicorn
from fastapi import FastAPI

from config.config import read

app = FastAPI()


if __name__ == "__main__":
    config = read('config.yaml')

    uvicorn.run("main:app", host="0.0.0.0", port=config['port'], reload=True)
