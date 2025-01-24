# coding: utf-8

"""
    Slurm REST API

    API to access and control Slurm

    The version of the OpenAPI document: Slurm-24.05.4&openapi/dbv0.0.39&openapi/slurmctld&openapi/slurmdbd&openapi/v0.0.39
    Contact: sales@schedmd.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, Field, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class SlurmV0041DeleteJobsRequest(BaseModel):
    """
    SlurmV0041DeleteJobsRequest
    """ # noqa: E501
    account: Optional[StrictStr] = Field(default=None, description="Filter jobs to a specific account")
    flags: Optional[List[StrictStr]] = Field(default=None, description="Filter jobs according to flags")
    job_name: Optional[StrictStr] = Field(default=None, description="Filter jobs to a specific name")
    jobs: Optional[List[StrictStr]] = Field(default=None, description="List of jobs to signal")
    partition: Optional[StrictStr] = Field(default=None, description="Filter jobs to a specific partition")
    qos: Optional[StrictStr] = Field(default=None, description="Filter jobs to a specific QOS")
    reservation: Optional[StrictStr] = Field(default=None, description="Filter jobs to a specific reservation")
    signal: Optional[StrictStr] = Field(default=None, description="Signal to send to jobs")
    job_state: Optional[List[StrictStr]] = Field(default=None, description="Filter jobs to a specific state")
    user_id: Optional[StrictStr] = Field(default=None, description="Filter jobs to a specific numeric user id")
    user_name: Optional[StrictStr] = Field(default=None, description="Filter jobs to a specific user name")
    wckey: Optional[StrictStr] = Field(default=None, description="Filter jobs to a specific wckey")
    nodes: Optional[List[StrictStr]] = Field(default=None, description="Filter jobs to a set of nodes")
    __properties: ClassVar[List[str]] = ["account", "flags", "job_name", "jobs", "partition", "qos", "reservation", "signal", "job_state", "user_id", "user_name", "wckey", "nodes"]

    @field_validator('flags')
    def flags_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        for i in value:
            if i not in set(['BATCH_JOB', 'ARRAY_TASK', 'FULL_STEPS_ONLY', 'FULL_JOB', 'FEDERATION_REQUEUE', 'HURRY', 'OUT_OF_MEMORY', 'NO_SIBLING_JOBS', 'RESERVATION_JOB', 'VERBOSE', 'CRON_JOBS', 'WARNING_SENT']):
                raise ValueError("each list item must be one of ('BATCH_JOB', 'ARRAY_TASK', 'FULL_STEPS_ONLY', 'FULL_JOB', 'FEDERATION_REQUEUE', 'HURRY', 'OUT_OF_MEMORY', 'NO_SIBLING_JOBS', 'RESERVATION_JOB', 'VERBOSE', 'CRON_JOBS', 'WARNING_SENT')")
        return value

    @field_validator('job_state')
    def job_state_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        for i in value:
            if i not in set(['PENDING', 'RUNNING', 'SUSPENDED', 'COMPLETED', 'CANCELLED', 'FAILED', 'TIMEOUT', 'NODE_FAIL', 'PREEMPTED', 'BOOT_FAIL', 'DEADLINE', 'OUT_OF_MEMORY', 'LAUNCH_FAILED', 'UPDATE_DB', 'REQUEUED', 'REQUEUE_HOLD', 'SPECIAL_EXIT', 'RESIZING', 'CONFIGURING', 'COMPLETING', 'STOPPED', 'RECONFIG_FAIL', 'POWER_UP_NODE', 'REVOKED', 'REQUEUE_FED', 'RESV_DEL_HOLD', 'SIGNALING', 'STAGE_OUT']):
                raise ValueError("each list item must be one of ('PENDING', 'RUNNING', 'SUSPENDED', 'COMPLETED', 'CANCELLED', 'FAILED', 'TIMEOUT', 'NODE_FAIL', 'PREEMPTED', 'BOOT_FAIL', 'DEADLINE', 'OUT_OF_MEMORY', 'LAUNCH_FAILED', 'UPDATE_DB', 'REQUEUED', 'REQUEUE_HOLD', 'SPECIAL_EXIT', 'RESIZING', 'CONFIGURING', 'COMPLETING', 'STOPPED', 'RECONFIG_FAIL', 'POWER_UP_NODE', 'REVOKED', 'REQUEUE_FED', 'RESV_DEL_HOLD', 'SIGNALING', 'STAGE_OUT')")
        return value

    model_config = {
        "populate_by_name": True,
        "validate_assignment": True,
        "protected_namespaces": (),
    }


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of SlurmV0041DeleteJobsRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of SlurmV0041DeleteJobsRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "account": obj.get("account"),
            "flags": obj.get("flags"),
            "job_name": obj.get("job_name"),
            "jobs": obj.get("jobs"),
            "partition": obj.get("partition"),
            "qos": obj.get("qos"),
            "reservation": obj.get("reservation"),
            "signal": obj.get("signal"),
            "job_state": obj.get("job_state"),
            "user_id": obj.get("user_id"),
            "user_name": obj.get("user_name"),
            "wckey": obj.get("wckey"),
            "nodes": obj.get("nodes")
        })
        return _obj


