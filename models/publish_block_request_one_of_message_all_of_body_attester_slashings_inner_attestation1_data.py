# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from models.get_state_finality_checkpoints_response_data_previous_justified import GetStateFinalityCheckpointsResponseDataPreviousJustified


class PublishBlockRequestOneOfMessageAllOfBodyAttesterSlashingsInnerAttestation1Data(BaseModel):
    """PublishBlockRequestOneOfMessageAllOfBodyAttesterSlashingsInnerAttestation1Data - a model defined in OpenAPI

        slot: The slot of this PublishBlockRequestOneOfMessageAllOfBodyAttesterSlashingsInnerAttestation1Data [Optional].
        index: The index of this PublishBlockRequestOneOfMessageAllOfBodyAttesterSlashingsInnerAttestation1Data [Optional].
        beacon_block_root: The beacon_block_root of this PublishBlockRequestOneOfMessageAllOfBodyAttesterSlashingsInnerAttestation1Data [Optional].
        source: The source of this PublishBlockRequestOneOfMessageAllOfBodyAttesterSlashingsInnerAttestation1Data [Optional].
        target: The target of this PublishBlockRequestOneOfMessageAllOfBodyAttesterSlashingsInnerAttestation1Data [Optional].
    """

    slot: Optional[str] = Field(alias="slot", default=None)
    index: Optional[str] = Field(alias="index", default=None)
    beacon_block_root: Optional[str] = Field(alias="beacon_block_root", default=None)
    source: Optional[GetStateFinalityCheckpointsResponseDataPreviousJustified] = Field(alias="source", default=None)
    target: Optional[GetStateFinalityCheckpointsResponseDataPreviousJustified] = Field(alias="target", default=None)

PublishBlockRequestOneOfMessageAllOfBodyAttesterSlashingsInnerAttestation1Data.update_forward_refs()
