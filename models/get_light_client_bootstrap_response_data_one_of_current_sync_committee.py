# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401


class GetLightClientBootstrapResponseDataOneOfCurrentSyncCommittee(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    GetLightClientBootstrapResponseDataOneOfCurrentSyncCommittee - a model defined in OpenAPI

        pubkeys: The pubkeys of this GetLightClientBootstrapResponseDataOneOfCurrentSyncCommittee [Optional].
        aggregate_pubkey: The aggregate_pubkey of this GetLightClientBootstrapResponseDataOneOfCurrentSyncCommittee [Optional].
    """

    pubkeys: Optional[List[str]] = Field(alias="pubkeys", default=None)
    aggregate_pubkey: Optional[str] = Field(alias="aggregate_pubkey", default=None)

    @validator("aggregate_pubkey")
    def aggregate_pubkey_pattern(cls, value):
        assert value is not None and re.match(r"^0x[a-fA-F0-9]{96}$", value)
        return value

GetLightClientBootstrapResponseDataOneOfCurrentSyncCommittee.update_forward_refs()
