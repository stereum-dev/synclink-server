"""
Schema definition of the hierarchical config files and CLI arguments.
"""
from typing import Dict, List, Optional
from pydantic import validator
from pydantic.dataclasses import dataclass # pydantic has more validation features than default dataclasses
from dataclasses import field
from omegaconf import MISSING, DictConfig
from .validate import validate

#
# OMEGACONF STRUCTURED CONFIG
#

# Main (Summary)
@dataclass
class Config:
    addr: str = "0.0.0.0"
    @validator("addr")
    def check_addr(cls, addr: str) -> str:
        return validate.addr(cls,addr)
    port: int = 8000
    @validator("port")
    def check_port(cls, port: int) -> int:
        return validate.port(cls,port)
    eth_api_address: str = "http://localhost:5051"
    @validator("eth_api_address")
    def check_eth_api_address(cls, eth_api_address: str) -> str:
        return validate.eth_api_address(cls,eth_api_address)
    config: str = "config.yaml"

#
# ARGPARSE COMMANDLINE ARGUMENTS
#

# Command Line Arguments (associated to omegaconf structured config)
# Important: this dict MUST follow the omegaconf definition above.
cli_args = {
    'addr': {
        'args': ["-a", "--addr"],
        'type': str,
        'dest' : 'addr',
        'default' : '0.0.0.0',
        #'required' : True, # just as example
        'help' : 'the ip address or domain of your synclink server',
    },
    'port': {
        'args': ["-p", "--port"],
        'type': int,
        'dest' : 'port',
        'default' : 8000,
        'help' : 'the port of your synclink erver',
    },
    'eth_api_address': {
        'args': ["-e", "--eth_api_address", "--api", "--node"],
        'type': str,
        'dest' : 'eth_api_address',
        'default' : "http://127.0.0.1:5051",
        'help' : 'the http address of your eth api node',
    },
    'config': {
        'args': ["-c", "--config", "--ccc"],
        'type': str,
        'dest' : 'config',
        'default' : "config.yaml",
        'help' : 'path to an optional config YAML file',
    },
}