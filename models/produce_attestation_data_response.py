# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from models.publish_block_request_one_of_message_all_of_body_attester_slashings_inner_attestation1_data import PublishBlockRequestOneOfMessageAllOfBodyAttesterSlashingsInnerAttestation1Data


class ProduceAttestationDataResponse(BaseModel):
    """ProduceAttestationDataResponse - a model defined in OpenAPI

        data: The data of this ProduceAttestationDataResponse [Optional].
    """

    data: Optional[PublishBlockRequestOneOfMessageAllOfBodyAttesterSlashingsInnerAttestation1Data] = Field(alias="data", default=None)

ProduceAttestationDataResponse.update_forward_refs()
