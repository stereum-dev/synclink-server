# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401


class AltairSyncCommitteeSubscription(BaseModel):
    """AltairSyncCommitteeSubscription - a model defined in OpenAPI

        validator_index: The validator_index of this AltairSyncCommitteeSubscription [Optional].
        sync_committee_indices: The sync_committee_indices of this AltairSyncCommitteeSubscription [Optional].
        until_epoch: The until_epoch of this AltairSyncCommitteeSubscription [Optional].
    """

    validator_index: Optional[str] = Field(alias="validator_index", default=None)
    sync_committee_indices: Optional[List[str]] = Field(alias="sync_committee_indices", default=None)
    until_epoch: Optional[str] = Field(alias="until_epoch", default=None)

AltairSyncCommitteeSubscription.update_forward_refs()
