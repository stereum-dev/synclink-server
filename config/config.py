import yaml
from pydantic import BaseModel


class AppConfig(BaseModel):
    port: int


def read(file_name):
    defaultConfig: AppConfig = {
        "port": 8000
    }

    with open(file_name, "r") as f:
        yamlConfig: AppConfig = yaml.load(f, Loader=yaml.FullLoader) or {}

    config: AppConfig = {**defaultConfig, **yamlConfig}

    return config
