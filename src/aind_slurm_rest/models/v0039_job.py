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

from pydantic import BaseModel, Field, StrictBool, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from aind_slurm_rest.models.v0039_assoc_short import V0039AssocShort
from aind_slurm_rest.models.v0039_job_array import V0039JobArray
from aind_slurm_rest.models.v0039_job_comment import V0039JobComment
from aind_slurm_rest.models.v0039_job_exit_code import V0039JobExitCode
from aind_slurm_rest.models.v0039_job_het import V0039JobHet
from aind_slurm_rest.models.v0039_job_mcs import V0039JobMcs
from aind_slurm_rest.models.v0039_job_required import V0039JobRequired
from aind_slurm_rest.models.v0039_job_reservation import V0039JobReservation
from aind_slurm_rest.models.v0039_job_state import V0039JobState
from aind_slurm_rest.models.v0039_job_time import V0039JobTime
from aind_slurm_rest.models.v0039_job_tres import V0039JobTres
from aind_slurm_rest.models.v0039_step import V0039Step
from aind_slurm_rest.models.v0039_uint32_no_val import V0039Uint32NoVal
from aind_slurm_rest.models.v0039_wckey_tag import V0039WckeyTag
from typing import Optional, Set
from typing_extensions import Self

class V0039Job(BaseModel):
    """
    V0039Job
    """ # noqa: E501
    account: Optional[StrictStr] = None
    comment: Optional[V0039JobComment] = None
    allocation_nodes: Optional[StrictInt] = None
    array: Optional[V0039JobArray] = None
    association: Optional[V0039AssocShort] = None
    block: Optional[StrictStr] = None
    cluster: Optional[StrictStr] = None
    constraints: Optional[StrictStr] = None
    container: Optional[StrictStr] = None
    derived_exit_code: Optional[V0039JobExitCode] = None
    time: Optional[V0039JobTime] = None
    exit_code: Optional[V0039JobExitCode] = None
    extra: Optional[StrictStr] = None
    failed_node: Optional[StrictStr] = None
    flags: Optional[List[StrictStr]] = None
    group: Optional[StrictStr] = None
    het: Optional[V0039JobHet] = None
    job_id: Optional[StrictInt] = None
    name: Optional[StrictStr] = None
    licenses: Optional[StrictStr] = None
    mcs: Optional[V0039JobMcs] = None
    nodes: Optional[StrictStr] = None
    partition: Optional[StrictStr] = None
    hold: Optional[StrictBool] = Field(default=None, description="Hold (true) or release (false) job")
    priority: Optional[V0039Uint32NoVal] = None
    qos: Optional[StrictStr] = None
    required: Optional[V0039JobRequired] = None
    kill_request_user: Optional[StrictStr] = None
    reservation: Optional[V0039JobReservation] = None
    script: Optional[StrictStr] = None
    state: Optional[V0039JobState] = None
    steps: Optional[List[V0039Step]] = None
    submit_line: Optional[StrictStr] = None
    tres: Optional[V0039JobTres] = None
    used_gres: Optional[StrictStr] = None
    user: Optional[StrictStr] = None
    wckey: Optional[V0039WckeyTag] = None
    working_directory: Optional[StrictStr] = None
    __properties: ClassVar[List[str]] = ["account", "comment", "allocation_nodes", "array", "association", "block", "cluster", "constraints", "container", "derived_exit_code", "time", "exit_code", "extra", "failed_node", "flags", "group", "het", "job_id", "name", "licenses", "mcs", "nodes", "partition", "hold", "priority", "qos", "required", "kill_request_user", "reservation", "script", "state", "steps", "submit_line", "tres", "used_gres", "user", "wckey", "working_directory"]

    @field_validator('flags')
    def flags_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        for i in value:
            if i not in set(['NONE', 'CLEAR_SCHEDULING', 'NOT_SET', 'STARTED_ON_SUBMIT', 'STARTED_ON_SCHEDULE', 'STARTED_ON_BACKFILL', 'START_RECEIVED']):
                raise ValueError("each list item must be one of ('NONE', 'CLEAR_SCHEDULING', 'NOT_SET', 'STARTED_ON_SUBMIT', 'STARTED_ON_SCHEDULE', 'STARTED_ON_BACKFILL', 'START_RECEIVED')")
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
        """Create an instance of V0039Job from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of comment
        if self.comment:
            _dict['comment'] = self.comment.to_dict()
        # override the default output from pydantic by calling `to_dict()` of array
        if self.array:
            _dict['array'] = self.array.to_dict()
        # override the default output from pydantic by calling `to_dict()` of association
        if self.association:
            _dict['association'] = self.association.to_dict()
        # override the default output from pydantic by calling `to_dict()` of derived_exit_code
        if self.derived_exit_code:
            _dict['derived_exit_code'] = self.derived_exit_code.to_dict()
        # override the default output from pydantic by calling `to_dict()` of time
        if self.time:
            _dict['time'] = self.time.to_dict()
        # override the default output from pydantic by calling `to_dict()` of exit_code
        if self.exit_code:
            _dict['exit_code'] = self.exit_code.to_dict()
        # override the default output from pydantic by calling `to_dict()` of het
        if self.het:
            _dict['het'] = self.het.to_dict()
        # override the default output from pydantic by calling `to_dict()` of mcs
        if self.mcs:
            _dict['mcs'] = self.mcs.to_dict()
        # override the default output from pydantic by calling `to_dict()` of priority
        if self.priority:
            _dict['priority'] = self.priority.to_dict()
        # override the default output from pydantic by calling `to_dict()` of required
        if self.required:
            _dict['required'] = self.required.to_dict()
        # override the default output from pydantic by calling `to_dict()` of reservation
        if self.reservation:
            _dict['reservation'] = self.reservation.to_dict()
        # override the default output from pydantic by calling `to_dict()` of state
        if self.state:
            _dict['state'] = self.state.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in steps (list)
        _items = []
        if self.steps:
            for _item in self.steps:
                if _item:
                    _items.append(_item.to_dict())
            _dict['steps'] = _items
        # override the default output from pydantic by calling `to_dict()` of tres
        if self.tres:
            _dict['tres'] = self.tres.to_dict()
        # override the default output from pydantic by calling `to_dict()` of wckey
        if self.wckey:
            _dict['wckey'] = self.wckey.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of V0039Job from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "account": obj.get("account"),
            "comment": V0039JobComment.from_dict(obj["comment"]) if obj.get("comment") is not None else None,
            "allocation_nodes": obj.get("allocation_nodes"),
            "array": V0039JobArray.from_dict(obj["array"]) if obj.get("array") is not None else None,
            "association": V0039AssocShort.from_dict(obj["association"]) if obj.get("association") is not None else None,
            "block": obj.get("block"),
            "cluster": obj.get("cluster"),
            "constraints": obj.get("constraints"),
            "container": obj.get("container"),
            "derived_exit_code": V0039JobExitCode.from_dict(obj["derived_exit_code"]) if obj.get("derived_exit_code") is not None else None,
            "time": V0039JobTime.from_dict(obj["time"]) if obj.get("time") is not None else None,
            "exit_code": V0039JobExitCode.from_dict(obj["exit_code"]) if obj.get("exit_code") is not None else None,
            "extra": obj.get("extra"),
            "failed_node": obj.get("failed_node"),
            "flags": obj.get("flags"),
            "group": obj.get("group"),
            "het": V0039JobHet.from_dict(obj["het"]) if obj.get("het") is not None else None,
            "job_id": obj.get("job_id"),
            "name": obj.get("name"),
            "licenses": obj.get("licenses"),
            "mcs": V0039JobMcs.from_dict(obj["mcs"]) if obj.get("mcs") is not None else None,
            "nodes": obj.get("nodes"),
            "partition": obj.get("partition"),
            "hold": obj.get("hold"),
            "priority": V0039Uint32NoVal.from_dict(obj["priority"]) if obj.get("priority") is not None else None,
            "qos": obj.get("qos"),
            "required": V0039JobRequired.from_dict(obj["required"]) if obj.get("required") is not None else None,
            "kill_request_user": obj.get("kill_request_user"),
            "reservation": V0039JobReservation.from_dict(obj["reservation"]) if obj.get("reservation") is not None else None,
            "script": obj.get("script"),
            "state": V0039JobState.from_dict(obj["state"]) if obj.get("state") is not None else None,
            "steps": [V0039Step.from_dict(_item) for _item in obj["steps"]] if obj.get("steps") is not None else None,
            "submit_line": obj.get("submit_line"),
            "tres": V0039JobTres.from_dict(obj["tres"]) if obj.get("tres") is not None else None,
            "used_gres": obj.get("used_gres"),
            "user": obj.get("user"),
            "wckey": V0039WckeyTag.from_dict(obj["wckey"]) if obj.get("wckey") is not None else None,
            "working_directory": obj.get("working_directory")
        })
        return _obj


