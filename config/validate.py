"""
Validator class for specific config types.
FIXME: for whetever reason validators fail on Mac with errors like:
AttributeError: module 'validators' has no attribute 'ip_address'
"""
import validators

class validate:

    @staticmethod
    def addr(cls, addr: str) -> str:
        # if addr != "localhost" and not validators.domain(addr) and not validators.ip_address.ipv4(addr) and not validators.ip_address.ipv6(addr):
        #     raise ValueError(f"'addr' must be a valid domain or IP, got: {addr}")
        return addr

    @staticmethod
    def port(cls, port: int) -> int:
        if port < 1024:
            raise ValueError(f"'port' must be non-privileged, got: {port}")
        return port

    @staticmethod
    def eth_api_address(cls, eth_api_address: str) -> str:
        # if not validators.url(eth_api_address):
        #     raise ValueError(f"'eth_api_address' must be a valid url, got: {eth_api_address}")
        return eth_api_address