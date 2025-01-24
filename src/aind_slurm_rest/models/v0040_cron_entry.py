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
from aind_slurm_rest.models.slurm_v0041_post_job_submit_request_jobs_inner_crontab_line import SlurmV0041PostJobSubmitRequestJobsInnerCrontabLine
from typing import Optional, Set
from typing_extensions import Self

class V0040CronEntry(BaseModel):
    """
    V0040CronEntry
    """ # noqa: E501
    flags: Optional[List[StrictStr]] = Field(default=None, description="Flags")
    minute: Optional[StrictStr] = Field(default=None, description="Ranged string specifying eligible minute values (e.g. 0-10,50)")
    hour: Optional[StrictStr] = Field(default=None, description="Ranged string specifying eligible hour values (e.g. 0-5,23)")
    day_of_month: Optional[StrictStr] = Field(default=None, description="Ranged string specifying eligible day of month values (e.g. 0-10,29)")
    month: Optional[StrictStr] = Field(default=None, description="Ranged string specifying eligible month values (e.g. 0-5,12)")
    day_of_week: Optional[StrictStr] = Field(default=None, description="Ranged string specifying eligible day of week values (e.g.0-3,7)")
    specification: Optional[StrictStr] = Field(default=None, description="Time specification (* means valid for all allowed values) - minute hour day_of_month month day_of_week")
    command: Optional[StrictStr] = Field(default=None, description="Command to run")
    line: Optional[SlurmV0041PostJobSubmitRequestJobsInnerCrontabLine] = None
    __properties: ClassVar[List[str]] = ["flags", "minute", "hour", "day_of_month", "month", "day_of_week", "specification", "command", "line"]

    @field_validator('flags')
    def flags_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        for i in value:
            if i not in set(['WILD_MINUTE', 'WILD_HOUR', 'WILD_DAY_OF_MONTH', 'WILD_MONTH', 'WILD_DAY_OF_WEEK']):
                raise ValueError("each list item must be one of ('WILD_MINUTE', 'WILD_HOUR', 'WILD_DAY_OF_MONTH', 'WILD_MONTH', 'WILD_DAY_OF_WEEK')")
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
        """Create an instance of V0040CronEntry from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of line
        if self.line:
            _dict['line'] = self.line.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of V0040CronEntry from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "flags": obj.get("flags"),
            "minute": obj.get("minute"),
            "hour": obj.get("hour"),
            "day_of_month": obj.get("day_of_month"),
            "month": obj.get("month"),
            "day_of_week": obj.get("day_of_week"),
            "specification": obj.get("specification"),
            "command": obj.get("command"),
            "line": SlurmV0041PostJobSubmitRequestJobsInnerCrontabLine.from_dict(obj["line"]) if obj.get("line") is not None else None
        })
        return _obj


