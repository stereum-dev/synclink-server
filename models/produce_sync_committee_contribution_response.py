# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from models.produce_sync_committee_contribution_response_data import ProduceSyncCommitteeContributionResponseData


class ProduceSyncCommitteeContributionResponse(BaseModel):
    """ProduceSyncCommitteeContributionResponse - a model defined in OpenAPI

        data: The data of this ProduceSyncCommitteeContributionResponse [Optional].
    """

    data: Optional[ProduceSyncCommitteeContributionResponseData] = Field(alias="data", default=None)

ProduceSyncCommitteeContributionResponse.update_forward_refs()
