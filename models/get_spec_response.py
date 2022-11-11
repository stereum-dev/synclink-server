# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401


class GetSpecResponseData(BaseModel):
    DEPOSIT_CONTRACT_ADDRESS: Optional[str] = Field(
        alias="DEPOSIT_CONTRACT_ADDRESS", default=None)

    PRESET_BASE: Optional[str] = Field(
        alias="PRESET_BASE", default=None)

    CONFIG_NAME: Optional[str] = Field(
        alias="CONFIG_NAME", default=None)

    DEPOSIT_CHAIN_ID: Optional[str] = Field(
        alias="DEPOSIT_CHAIN_ID", default=None)

    SAFE_SLOTS_TO_UPDATE_JUSTIFIED: Optional[str] = Field(
        alias="SAFE_SLOTS_TO_UPDATE_JUSTIFIED", default=None)

    SLOTS_PER_EPOCH: Optional[str] = Field(
        alias="SLOTS_PER_EPOCH", default=None)

    EPOCHS_PER_SYNC_COMMITTEE_PERIOD: Optional[str] = Field(
        alias="EPOCHS_PER_SYNC_COMMITTEE_PERIOD", default=None)

    MIN_SYNC_COMMITTEE_PARTICIPANTS: Optional[str] = Field(
        alias="MIN_SYNC_COMMITTEE_PARTICIPANTS", default=None)

    TARGET_COMMITTEE_SIZE: Optional[str] = Field(
        alias="TARGET_COMMITTEE_SIZE", default=None)

    SYNC_COMMITTEE_SIZE: Optional[str] = Field(
        alias="SYNC_COMMITTEE_SIZE", default=None)

    TERMINAL_BLOCK_HASH_ACTIVATION_EPOCH: Optional[str] = Field(
        alias="TERMINAL_BLOCK_HASH_ACTIVATION_EPOCH", default=None)

    MAX_VALIDATORS_PER_COMMITTEE: Optional[str] = Field(
        alias="MAX_VALIDATORS_PER_COMMITTEE", default=None)

    BASE_REWARD_FACTOR: Optional[str] = Field(
        alias="BASE_REWARD_FACTOR", default=None)

    EFFECTIVE_BALANCE_INCREMENT: Optional[str] = Field(
        alias="EFFECTIVE_BALANCE_INCREMENT", default=None)

    MAX_EFFECTIVE_BALANCE: Optional[str] = Field(
        alias="MAX_EFFECTIVE_BALANCE", default=None)

    MIN_DEPOSIT_AMOUNT: Optional[str] = Field(
        alias="MIN_DEPOSIT_AMOUNT", default=None)

    MAX_ATTESTATIONS: Optional[str] = Field(
        alias="MAX_ATTESTATIONS", default=None)

    SECONDS_PER_ETH1_BLOCK: Optional[str] = Field(
        alias="SECONDS_PER_ETH1_BLOCK", default=None)

    GENESIS_DELAY: Optional[str] = Field(
        alias="GENESIS_DELAY", default=None)

    SECONDS_PER_SLOT: Optional[str] = Field(
        alias="SECONDS_PER_SLOT", default=None)

    MAX_DEPOSITS: Optional[str] = Field(
        alias="MAX_DEPOSITS", default=None)

    MIN_GENESIS_ACTIVE_VALIDATOR_COUNT: Optional[str] = Field(
        alias="MIN_GENESIS_ACTIVE_VALIDATOR_COUNT", default=None)

    ETH1_FOLLOW_DISTANCE: Optional[str] = Field(
        alias="ETH1_FOLLOW_DISTANCE", default=None)


GetSpecResponseData.update_forward_refs()


class GetSpecResponse(BaseModel):
    """GetSpecResponse - a model defined in OpenAPI

        data: The data of this GetSpecResponse [Optional].
    """

    data: Optional[GetSpecResponseData] = Field(alias="data", default=None)


GetSpecResponse.update_forward_refs()
