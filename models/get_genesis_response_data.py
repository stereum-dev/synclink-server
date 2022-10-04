# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401


class GetGenesisResponseData(BaseModel):
    """GetGenesisResponseData - a model defined in OpenAPI

        genesis_time: The genesis_time of this GetGenesisResponseData [Optional].
        genesis_validators_root: The genesis_validators_root of this GetGenesisResponseData [Optional].
        genesis_fork_version: The genesis_fork_version of this GetGenesisResponseData [Optional].
    """

    genesis_time: Optional[str] = Field(alias="genesis_time", default=None)
    genesis_validators_root: Optional[str] = Field(alias="genesis_validators_root", default=None)
    genesis_fork_version: Optional[str] = Field(alias="genesis_fork_version", default=None)

    @validator("genesis_validators_root")
    def genesis_validators_root_pattern(cls, value):
        assert value is not None and re.match(r"^0x[a-fA-F0-9]{64}$", value)
        return value

    @validator("genesis_fork_version")
    def genesis_fork_version_pattern(cls, value):
        assert value is not None and re.match(r"^0x[a-fA-F0-9]{8}$", value)
        return value

GetGenesisResponseData.update_forward_refs()
