# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from models.beacon_block_all_of_body import BeaconBlockAllOfBody


class BeaconBlock(BaseModel):
    """BeaconBlock - a model defined in OpenAPI

        slot: The slot of this BeaconBlock [Optional].
        proposer_index: The proposer_index of this BeaconBlock [Optional].
        parent_root: The parent_root of this BeaconBlock [Optional].
        state_root: The state_root of this BeaconBlock [Optional].
        body: The body of this BeaconBlock [Optional].
    """

    slot: Optional[str] = Field(alias="slot", default=None)
    proposer_index: Optional[str] = Field(alias="proposer_index", default=None)
    parent_root: Optional[str] = Field(alias="parent_root", default=None)
    state_root: Optional[str] = Field(alias="state_root", default=None)
    body: Optional[BeaconBlockAllOfBody] = Field(alias="body", default=None)

BeaconBlock.update_forward_refs()
