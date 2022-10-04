# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from models.publish_block_request_one_of_message_all_of_body_attester_slashings_inner_attestation1_data import PublishBlockRequestOneOfMessageAllOfBodyAttesterSlashingsInnerAttestation1Data


class GetStateResponseDataPreviousEpochAttestationsInner(BaseModel):
    """GetStateResponseDataPreviousEpochAttestationsInner - a model defined in OpenAPI

        aggregation_bits: The aggregation_bits of this GetStateResponseDataPreviousEpochAttestationsInner [Optional].
        data: The data of this GetStateResponseDataPreviousEpochAttestationsInner [Optional].
        inclusion_delay: The inclusion_delay of this GetStateResponseDataPreviousEpochAttestationsInner [Optional].
        proposer_index: The proposer_index of this GetStateResponseDataPreviousEpochAttestationsInner [Optional].
    """

    aggregation_bits: Optional[str] = Field(alias="aggregation_bits", default=None)
    data: Optional[PublishBlockRequestOneOfMessageAllOfBodyAttesterSlashingsInnerAttestation1Data] = Field(alias="data", default=None)
    inclusion_delay: Optional[str] = Field(alias="inclusion_delay", default=None)
    proposer_index: Optional[str] = Field(alias="proposer_index", default=None)

    @validator("aggregation_bits")
    def aggregation_bits_pattern(cls, value):
        assert value is not None and re.match(r"^0x[a-fA-F0-9]+$", value)
        return value

GetStateResponseDataPreviousEpochAttestationsInner.update_forward_refs()
