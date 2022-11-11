# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401


class GetSyncCommitteeDutiesResponseDataInner(BaseModel):
    """GetSyncCommitteeDutiesResponseDataInner - a model defined in OpenAPI

        pubkey: The pubkey of this GetSyncCommitteeDutiesResponseDataInner [Optional].
        validator_index: The validator_index of this GetSyncCommitteeDutiesResponseDataInner [Optional].
        validator_sync_committee_indices: The validator_sync_committee_indices of this GetSyncCommitteeDutiesResponseDataInner [Optional].
    """

    pubkey: Optional[str] = Field(alias="pubkey", default=None)
    validator_index: Optional[str] = Field(alias="validator_index", default=None)
    validator_sync_committee_indices: Optional[List[str]] = Field(alias="validator_sync_committee_indices", default=None)

    @validator("pubkey")
    def pubkey_pattern(cls, value):
        assert value is not None and re.match(r"^0x[a-fA-F0-9]{96}$", value)
        return value

GetSyncCommitteeDutiesResponseDataInner.update_forward_refs()
