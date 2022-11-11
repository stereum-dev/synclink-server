# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from models.get_block_headers_response_data_inner_header_message import GetBlockHeadersResponseDataInnerHeaderMessage
from models.get_state_finality_checkpoints_response_data_previous_justified import GetStateFinalityCheckpointsResponseDataPreviousJustified
from models.get_state_fork_response_data import GetStateForkResponseData
from models.get_state_response_data_eth1_data_votes_inner import GetStateResponseDataEth1DataVotesInner
from models.get_state_response_data_previous_epoch_attestations_inner import GetStateResponseDataPreviousEpochAttestationsInner
from models.get_state_response_data_validators_inner import GetStateResponseDataValidatorsInner
from models.publish_block_request_one_of_message_all_of_body_eth1_data import PublishBlockRequestOneOfMessageAllOfBodyEth1Data


class GetStateResponseData(BaseModel):
    """GetStateResponseData - a model defined in OpenAPI

        genesis_time: The genesis_time of this GetStateResponseData [Optional].
        genesis_validators_root: The genesis_validators_root of this GetStateResponseData [Optional].
        slot: The slot of this GetStateResponseData [Optional].
        fork: The fork of this GetStateResponseData [Optional].
        latest_block_header: The latest_block_header of this GetStateResponseData [Optional].
        block_roots: The block_roots of this GetStateResponseData [Optional].
        state_roots: The state_roots of this GetStateResponseData [Optional].
        historical_roots: The historical_roots of this GetStateResponseData [Optional].
        eth1_data: The eth1_data of this GetStateResponseData [Optional].
        eth1_data_votes: The eth1_data_votes of this GetStateResponseData [Optional].
        eth1_deposit_index: The eth1_deposit_index of this GetStateResponseData [Optional].
        validators: The validators of this GetStateResponseData [Optional].
        balances: The balances of this GetStateResponseData [Optional].
        randao_mixes: The randao_mixes of this GetStateResponseData [Optional].
        slashings: The slashings of this GetStateResponseData [Optional].
        previous_epoch_attestations: The previous_epoch_attestations of this GetStateResponseData [Optional].
        current_epoch_attestations: The current_epoch_attestations of this GetStateResponseData [Optional].
        justification_bits: The justification_bits of this GetStateResponseData [Optional].
        previous_justified_checkpoint: The previous_justified_checkpoint of this GetStateResponseData [Optional].
        current_justified_checkpoint: The current_justified_checkpoint of this GetStateResponseData [Optional].
        finalized_checkpoint: The finalized_checkpoint of this GetStateResponseData [Optional].
    """

    genesis_time: Optional[str] = Field(alias="genesis_time", default=None)
    genesis_validators_root: Optional[str] = Field(alias="genesis_validators_root", default=None)
    slot: Optional[str] = Field(alias="slot", default=None)
    fork: Optional[GetStateForkResponseData] = Field(alias="fork", default=None)
    latest_block_header: Optional[GetBlockHeadersResponseDataInnerHeaderMessage] = Field(alias="latest_block_header", default=None)
    block_roots: Optional[List[str]] = Field(alias="block_roots", default=None)
    state_roots: Optional[List[str]] = Field(alias="state_roots", default=None)
    historical_roots: Optional[List[str]] = Field(alias="historical_roots", default=None)
    eth1_data: Optional[PublishBlockRequestOneOfMessageAllOfBodyEth1Data] = Field(alias="eth1_data", default=None)
    eth1_data_votes: Optional[List[GetStateResponseDataEth1DataVotesInner]] = Field(alias="eth1_data_votes", default=None)
    eth1_deposit_index: Optional[str] = Field(alias="eth1_deposit_index", default=None)
    validators: Optional[List[GetStateResponseDataValidatorsInner]] = Field(alias="validators", default=None)
    balances: Optional[List[str]] = Field(alias="balances", default=None)
    randao_mixes: Optional[List[str]] = Field(alias="randao_mixes", default=None)
    slashings: Optional[List[str]] = Field(alias="slashings", default=None)
    previous_epoch_attestations: Optional[List[GetStateResponseDataPreviousEpochAttestationsInner]] = Field(alias="previous_epoch_attestations", default=None)
    current_epoch_attestations: Optional[List[GetStateResponseDataPreviousEpochAttestationsInner]] = Field(alias="current_epoch_attestations", default=None)
    justification_bits: Optional[str] = Field(alias="justification_bits", default=None)
    previous_justified_checkpoint: Optional[GetStateFinalityCheckpointsResponseDataPreviousJustified] = Field(alias="previous_justified_checkpoint", default=None)
    current_justified_checkpoint: Optional[GetStateFinalityCheckpointsResponseDataPreviousJustified] = Field(alias="current_justified_checkpoint", default=None)
    finalized_checkpoint: Optional[GetStateFinalityCheckpointsResponseDataPreviousJustified] = Field(alias="finalized_checkpoint", default=None)

    @validator("genesis_validators_root")
    def genesis_validators_root_pattern(cls, value):
        assert value is not None and re.match(r"^0x[a-fA-F0-9]{64}$", value)
        return value

    @validator("justification_bits")
    def justification_bits_pattern(cls, value):
        assert value is not None and re.match(r"^0x[a-fA-F0-9]+$", value)
        return value

GetStateResponseData.update_forward_refs()
