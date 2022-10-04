# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401


class GetBlockHeadersResponseDataInnerHeaderMessageAllOf(BaseModel):
    """GetBlockHeadersResponseDataInnerHeaderMessageAllOf - a model defined in OpenAPI

        slot: The slot of this GetBlockHeadersResponseDataInnerHeaderMessageAllOf [Optional].
        proposer_index: The proposer_index of this GetBlockHeadersResponseDataInnerHeaderMessageAllOf [Optional].
        parent_root: The parent_root of this GetBlockHeadersResponseDataInnerHeaderMessageAllOf [Optional].
        state_root: The state_root of this GetBlockHeadersResponseDataInnerHeaderMessageAllOf [Optional].
    """

    slot: Optional[str] = Field(alias="slot", default=None)
    proposer_index: Optional[str] = Field(alias="proposer_index", default=None)
    parent_root: Optional[str] = Field(alias="parent_root", default=None)
    state_root: Optional[str] = Field(alias="state_root", default=None)

GetBlockHeadersResponseDataInnerHeaderMessageAllOf.update_forward_refs()
