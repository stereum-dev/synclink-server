# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from models.publish_block_request_one_of_message_all_of_body_attester_slashings_inner_attestation1_data import PublishBlockRequestOneOfMessageAllOfBodyAttesterSlashingsInnerAttestation1Data


class PublishBlockRequestOneOfMessageAllOfBodyAttesterSlashingsInnerAttestation1(BaseModel):
    """PublishBlockRequestOneOfMessageAllOfBodyAttesterSlashingsInnerAttestation1 - a model defined in OpenAPI

        attesting_indices: The attesting_indices of this PublishBlockRequestOneOfMessageAllOfBodyAttesterSlashingsInnerAttestation1 [Optional].
        signature: The signature of this PublishBlockRequestOneOfMessageAllOfBodyAttesterSlashingsInnerAttestation1 [Optional].
        data: The data of this PublishBlockRequestOneOfMessageAllOfBodyAttesterSlashingsInnerAttestation1 [Optional].
    """

    attesting_indices: Optional[List[str]] = Field(alias="attesting_indices", default=None)
    signature: Optional[str] = Field(alias="signature", default=None)
    data: Optional[PublishBlockRequestOneOfMessageAllOfBodyAttesterSlashingsInnerAttestation1Data] = Field(alias="data", default=None)

PublishBlockRequestOneOfMessageAllOfBodyAttesterSlashingsInnerAttestation1.update_forward_refs()
