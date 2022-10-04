import string
import yaml
from pydantic import BaseModel


class AppConfig(BaseModel):
    port: int
    eth_api_address: str


def read(file_name):
    defaultConfig: AppConfig = {
        "port": 8000,
        "eth_api_address": "http://localhost:5051",
    }

    with open(file_name, "r") as f:
        yamlConfig: AppConfig = yaml.load(f, Loader=yaml.FullLoader) or {}

    config: AppConfig = {**defaultConfig, **yamlConfig}

    return config
