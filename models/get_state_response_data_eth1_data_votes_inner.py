# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401


class GetStateResponseDataEth1DataVotesInner(BaseModel):
    """GetStateResponseDataEth1DataVotesInner - a model defined in OpenAPI

        deposit_root: The deposit_root of this GetStateResponseDataEth1DataVotesInner [Optional].
        deposit_count: The deposit_count of this GetStateResponseDataEth1DataVotesInner [Optional].
        block_hash: The block_hash of this GetStateResponseDataEth1DataVotesInner [Optional].
    """

    deposit_root: Optional[str] = Field(alias="deposit_root", default=None)
    deposit_count: Optional[str] = Field(alias="deposit_count", default=None)
    block_hash: Optional[str] = Field(alias="block_hash", default=None)

GetStateResponseDataEth1DataVotesInner.update_forward_refs()
