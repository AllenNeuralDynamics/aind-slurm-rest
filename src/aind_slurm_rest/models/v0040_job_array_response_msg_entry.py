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

from pydantic import BaseModel, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class V0040JobArrayResponseMsgEntry(BaseModel):
    """
    V0040JobArrayResponseMsgEntry
    """ # noqa: E501
    job_id: Optional[StrictInt] = Field(default=None, description="Job ID for updated Job")
    step_id: Optional[StrictStr] = Field(default=None, description="Step ID for updated Job")
    error: Optional[StrictStr] = Field(default=None, description="Verbose update status or error")
    error_code: Optional[StrictInt] = Field(default=None, description="Verbose update status or error")
    why: Optional[StrictStr] = Field(default=None, description="Update response message")
    __properties: ClassVar[List[str]] = ["job_id", "step_id", "error", "error_code", "why"]

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
        """Create an instance of V0040JobArrayResponseMsgEntry from a JSON string"""
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
        """Create an instance of V0040JobArrayResponseMsgEntry from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "job_id": obj.get("job_id"),
            "step_id": obj.get("step_id"),
            "error": obj.get("error"),
            "error_code": obj.get("error_code"),
            "why": obj.get("why")
        })
        return _obj


