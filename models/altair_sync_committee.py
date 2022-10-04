# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401


class AltairSyncCommittee(BaseModel):
    """AltairSyncCommittee - a model defined in OpenAPI

        validators: The validators of this AltairSyncCommittee [Optional].
        validator_aggregates: The validator_aggregates of this AltairSyncCommittee [Optional].
    """

    validators: Optional[List] = Field(alias="validators", default=None)
    validator_aggregates: Optional[List[List]] = Field(alias="validator_aggregates", default=None)

AltairSyncCommittee.update_forward_refs()
