# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401


class GetPeerCountResponseData(BaseModel):
    """GetPeerCountResponseData - a model defined in OpenAPI

        disconnected: The disconnected of this GetPeerCountResponseData [Optional].
        connecting: The connecting of this GetPeerCountResponseData [Optional].
        connected: The connected of this GetPeerCountResponseData [Optional].
        disconnecting: The disconnecting of this GetPeerCountResponseData [Optional].
    """

    disconnected: Optional[str] = Field(alias="disconnected", default=None)
    connecting: Optional[str] = Field(alias="connecting", default=None)
    connected: Optional[str] = Field(alias="connected", default=None)
    disconnecting: Optional[str] = Field(alias="disconnecting", default=None)

GetPeerCountResponseData.update_forward_refs()
