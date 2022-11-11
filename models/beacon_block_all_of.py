# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from models.beacon_block_all_of_body import BeaconBlockAllOfBody


class BeaconBlockAllOf(BaseModel):
    """BeaconBlockAllOf - a model defined in OpenAPI

        body: The body of this BeaconBlockAllOf [Optional].
    """

    body: Optional[BeaconBlockAllOfBody] = Field(alias="body", default=None)

BeaconBlockAllOf.update_forward_refs()
