# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401


class Peer(BaseModel):
    """Peer - a model defined in OpenAPI

        peer_id: The peer_id of this Peer [Optional].
        enr: The enr of this Peer [Optional].
        last_seen_p2p_address: The last_seen_p2p_address of this Peer [Optional].
        state: The state of this Peer [Optional].
        direction: The direction of this Peer [Optional].
    """

    peer_id: Optional[str] = Field(alias="peer_id", default=None)
    enr: Optional[str] = Field(alias="enr", default=None)
    last_seen_p2p_address: Optional[str] = Field(alias="last_seen_p2p_address", default=None)
    state: Optional[str] = Field(alias="state", default=None)
    direction: Optional[str] = Field(alias="direction", default=None)

Peer.update_forward_refs()
