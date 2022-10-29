import yaml
from pydantic import BaseModel, Field


class AppConfig(BaseModel):
    addr: str = Field(alias="addr", default="0.0.0.0")
    port: int = Field(alias="port", default=8000)
    eth_api_address: str = Field(alias="eth_api_address",
                                 default='http://localhost:5051')


def read(file_name):
    defaultConfig: AppConfig = {
        "addr": "0.0.0.0",
        "port": 8000,
        "eth_api_address": "http://localhost:5051",
    }

    with open(file_name, "r") as f:
        yamlConfig: AppConfig = yaml.load(f, Loader=yaml.FullLoader) or {}

    config = AppConfig(**{**defaultConfig, **yamlConfig})

    return config
