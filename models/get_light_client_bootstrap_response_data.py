# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from models.get_light_client_bootstrap_response_data_one_of import GetLightClientBootstrapResponseDataOneOf
from models.get_light_client_bootstrap_response_data_one_of1 import GetLightClientBootstrapResponseDataOneOf1
from models.get_light_client_bootstrap_response_data_one_of1_header import GetLightClientBootstrapResponseDataOneOf1Header
from models.get_light_client_bootstrap_response_data_one_of_current_sync_committee import GetLightClientBootstrapResponseDataOneOfCurrentSyncCommittee


class GetLightClientBootstrapResponseData(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    GetLightClientBootstrapResponseData - a model defined in OpenAPI

        header: The header of this GetLightClientBootstrapResponseData [Optional].
        current_sync_committee: The current_sync_committee of this GetLightClientBootstrapResponseData [Optional].
        current_sync_committee_branch: The current_sync_committee_branch of this GetLightClientBootstrapResponseData [Optional].
    """

    header: Optional[GetLightClientBootstrapResponseDataOneOf1Header] = Field(alias="header", default=None)
    current_sync_committee: Optional[GetLightClientBootstrapResponseDataOneOfCurrentSyncCommittee] = Field(alias="current_sync_committee", default=None)
    current_sync_committee_branch: Optional[List[str]] = Field(alias="current_sync_committee_branch", default=None)

GetLightClientBootstrapResponseData.update_forward_refs()
