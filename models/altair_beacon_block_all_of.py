# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from models.altair_beacon_block_all_of_body import AltairBeaconBlockAllOfBody


class AltairBeaconBlockAllOf(BaseModel):
    """AltairBeaconBlockAllOf - a model defined in OpenAPI

        body: The body of this AltairBeaconBlockAllOf [Optional].
    """

    body: Optional[AltairBeaconBlockAllOfBody] = Field(alias="body", default=None)

AltairBeaconBlockAllOf.update_forward_refs()
