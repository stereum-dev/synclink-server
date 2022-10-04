# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from models.publish_block_request_one_of_message_all_of_body_attester_slashings_inner_attestation1 import PublishBlockRequestOneOfMessageAllOfBodyAttesterSlashingsInnerAttestation1


class AttesterSlashing(BaseModel):
    """AttesterSlashing - a model defined in OpenAPI

        attestation_1: The attestation_1 of this AttesterSlashing [Optional].
        attestation_2: The attestation_2 of this AttesterSlashing [Optional].
    """

    attestation_1: Optional[PublishBlockRequestOneOfMessageAllOfBodyAttesterSlashingsInnerAttestation1] = Field(alias="attestation_1", default=None)
    attestation_2: Optional[PublishBlockRequestOneOfMessageAllOfBodyAttesterSlashingsInnerAttestation1] = Field(alias="attestation_2", default=None)

AttesterSlashing.update_forward_refs()
