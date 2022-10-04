# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401


class SubmitPoolSyncCommitteeSignaturesRequestInner(BaseModel):
    """SubmitPoolSyncCommitteeSignaturesRequestInner - a model defined in OpenAPI

        slot: The slot of this SubmitPoolSyncCommitteeSignaturesRequestInner [Optional].
        beacon_block_root: The beacon_block_root of this SubmitPoolSyncCommitteeSignaturesRequestInner [Optional].
        validator_index: The validator_index of this SubmitPoolSyncCommitteeSignaturesRequestInner [Optional].
        signature: The signature of this SubmitPoolSyncCommitteeSignaturesRequestInner [Optional].
    """

    slot: Optional[str] = Field(alias="slot", default=None)
    beacon_block_root: Optional[str] = Field(alias="beacon_block_root", default=None)
    validator_index: Optional[str] = Field(alias="validator_index", default=None)
    signature: Optional[str] = Field(alias="signature", default=None)

    @validator("beacon_block_root")
    def beacon_block_root_pattern(cls, value):
        assert value is not None and re.match(r"^0x[a-fA-F0-9]{64}$", value)
        return value

    @validator("signature")
    def signature_pattern(cls, value):
        assert value is not None and re.match(r"^0x[a-fA-F0-9]{192}$", value)
        return value

SubmitPoolSyncCommitteeSignaturesRequestInner.update_forward_refs()
