# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401


class GetNetworkIdentityResponseDataMetadata(BaseModel):
    """GetNetworkIdentityResponseDataMetadata - a model defined in OpenAPI

        seq_number: The seq_number of this GetNetworkIdentityResponseDataMetadata [Optional].
        attnets: The attnets of this GetNetworkIdentityResponseDataMetadata [Optional].
        syncnets: The syncnets of this GetNetworkIdentityResponseDataMetadata [Optional].
    """

    seq_number: Optional[object] = Field(alias="seq_number", default=None)
    attnets: Optional[object] = Field(alias="attnets", default=None)
    syncnets: Optional[object] = Field(alias="syncnets", default=None)

GetNetworkIdentityResponseDataMetadata.update_forward_refs()
