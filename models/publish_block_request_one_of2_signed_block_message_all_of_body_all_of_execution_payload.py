# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from models.publish_block_request_one_of1_message_all_of_body_all_of_execution_payload_all_of_withdrawals_inner import PublishBlockRequestOneOf1MessageAllOfBodyAllOfExecutionPayloadAllOfWithdrawalsInner


class PublishBlockRequestOneOf2SignedBlockMessageAllOfBodyAllOfExecutionPayload(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    PublishBlockRequestOneOf2SignedBlockMessageAllOfBodyAllOfExecutionPayload - a model defined in OpenAPI

        parent_hash: The parent_hash of this PublishBlockRequestOneOf2SignedBlockMessageAllOfBodyAllOfExecutionPayload [Optional].
        fee_recipient: The fee_recipient of this PublishBlockRequestOneOf2SignedBlockMessageAllOfBodyAllOfExecutionPayload [Optional].
        state_root: The state_root of this PublishBlockRequestOneOf2SignedBlockMessageAllOfBodyAllOfExecutionPayload [Optional].
        receipts_root: The receipts_root of this PublishBlockRequestOneOf2SignedBlockMessageAllOfBodyAllOfExecutionPayload [Optional].
        logs_bloom: The logs_bloom of this PublishBlockRequestOneOf2SignedBlockMessageAllOfBodyAllOfExecutionPayload [Optional].
        prev_randao: The prev_randao of this PublishBlockRequestOneOf2SignedBlockMessageAllOfBodyAllOfExecutionPayload [Optional].
        block_number: The block_number of this PublishBlockRequestOneOf2SignedBlockMessageAllOfBodyAllOfExecutionPayload [Optional].
        gas_limit: The gas_limit of this PublishBlockRequestOneOf2SignedBlockMessageAllOfBodyAllOfExecutionPayload [Optional].
        gas_used: The gas_used of this PublishBlockRequestOneOf2SignedBlockMessageAllOfBodyAllOfExecutionPayload [Optional].
        timestamp: The timestamp of this PublishBlockRequestOneOf2SignedBlockMessageAllOfBodyAllOfExecutionPayload [Optional].
        extra_data: The extra_data of this PublishBlockRequestOneOf2SignedBlockMessageAllOfBodyAllOfExecutionPayload [Optional].
        base_fee_per_gas: The base_fee_per_gas of this PublishBlockRequestOneOf2SignedBlockMessageAllOfBodyAllOfExecutionPayload [Optional].
        excess_data_gas: The excess_data_gas of this PublishBlockRequestOneOf2SignedBlockMessageAllOfBodyAllOfExecutionPayload [Optional].
        block_hash: The block_hash of this PublishBlockRequestOneOf2SignedBlockMessageAllOfBodyAllOfExecutionPayload [Optional].
        transactions: The transactions of this PublishBlockRequestOneOf2SignedBlockMessageAllOfBodyAllOfExecutionPayload [Optional].
        withdrawals: The withdrawals of this PublishBlockRequestOneOf2SignedBlockMessageAllOfBodyAllOfExecutionPayload [Optional].
    """

    parent_hash: Optional[str] = Field(alias="parent_hash", default=None)
    fee_recipient: Optional[str] = Field(alias="fee_recipient", default=None)
    state_root: Optional[str] = Field(alias="state_root", default=None)
    receipts_root: Optional[str] = Field(alias="receipts_root", default=None)
    logs_bloom: Optional[str] = Field(alias="logs_bloom", default=None)
    prev_randao: Optional[str] = Field(alias="prev_randao", default=None)
    block_number: Optional[str] = Field(alias="block_number", default=None)
    gas_limit: Optional[str] = Field(alias="gas_limit", default=None)
    gas_used: Optional[str] = Field(alias="gas_used", default=None)
    timestamp: Optional[str] = Field(alias="timestamp", default=None)
    extra_data: Optional[str] = Field(alias="extra_data", default=None)
    base_fee_per_gas: Optional[str] = Field(alias="base_fee_per_gas", default=None)
    excess_data_gas: Optional[str] = Field(alias="excess_data_gas", default=None)
    block_hash: Optional[str] = Field(alias="block_hash", default=None)
    transactions: Optional[List[str]] = Field(alias="transactions", default=None)
    withdrawals: Optional[List[PublishBlockRequestOneOf1MessageAllOfBodyAllOfExecutionPayloadAllOfWithdrawalsInner]] = Field(alias="withdrawals", default=None)

    @validator("parent_hash")
    def parent_hash_pattern(cls, value):
        assert value is not None and re.match(r"^0x[a-fA-F0-9]{64}$", value)
        return value

    @validator("fee_recipient")
    def fee_recipient_pattern(cls, value):
        assert value is not None and re.match(r"^0x[a-fA-F0-9]{40}$", value)
        return value

    @validator("state_root")
    def state_root_pattern(cls, value):
        assert value is not None and re.match(r"^0x[a-fA-F0-9]{64}$", value)
        return value

    @validator("receipts_root")
    def receipts_root_pattern(cls, value):
        assert value is not None and re.match(r"^0x[a-fA-F0-9]{64}$", value)
        return value

    @validator("logs_bloom")
    def logs_bloom_pattern(cls, value):
        assert value is not None and re.match(r"^0x[a-fA-F0-9]{512}$", value)
        return value

    @validator("prev_randao")
    def prev_randao_pattern(cls, value):
        assert value is not None and re.match(r"^0x[a-fA-F0-9]{64}$", value)
        return value

    @validator("extra_data")
    def extra_data_pattern(cls, value):
        assert value is not None and re.match(r"^0x[a-fA-F0-9]{0,64}$", value)
        return value

    @validator("block_hash")
    def block_hash_pattern(cls, value):
        assert value is not None and re.match(r"^0x[a-fA-F0-9]{64}$", value)
        return value

PublishBlockRequestOneOf2SignedBlockMessageAllOfBodyAllOfExecutionPayload.update_forward_refs()