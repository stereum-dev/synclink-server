# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401


class BellatrixBeaconBlockAllOf(BaseModel):
    """BellatrixBeaconBlockAllOf - a model defined in OpenAPI

        body: The body of this BellatrixBeaconBlockAllOf [Optional].
    """

    body: Optional[object] = Field(alias="body", default=None)

BellatrixBeaconBlockAllOf.update_forward_refs()
