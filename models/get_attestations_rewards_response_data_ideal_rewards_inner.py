# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401


class GetAttestationsRewardsResponseDataIdealRewardsInner(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    GetAttestationsRewardsResponseDataIdealRewardsInner - a model defined in OpenAPI

        effective_balance: The effective_balance of this GetAttestationsRewardsResponseDataIdealRewardsInner.
        head: The head of this GetAttestationsRewardsResponseDataIdealRewardsInner.
        target: The target of this GetAttestationsRewardsResponseDataIdealRewardsInner.
        source: The source of this GetAttestationsRewardsResponseDataIdealRewardsInner.
        inclusion_delay: The inclusion_delay of this GetAttestationsRewardsResponseDataIdealRewardsInner [Optional].
        inactivity: The inactivity of this GetAttestationsRewardsResponseDataIdealRewardsInner.
    """

    effective_balance: str = Field(alias="effective_balance")
    head: str = Field(alias="head")
    target: str = Field(alias="target")
    source: str = Field(alias="source")
    inclusion_delay: Optional[str] = Field(alias="inclusion_delay", default=None)
    inactivity: str = Field(alias="inactivity")

GetAttestationsRewardsResponseDataIdealRewardsInner.update_forward_refs()
