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

from pydantic import BaseModel, Field, StrictInt
from typing import Any, ClassVar, Dict, List, Optional
from aind_slurm_rest.models.v0040_job_time_system import V0040JobTimeSystem
from aind_slurm_rest.models.v0040_job_time_total import V0040JobTimeTotal
from aind_slurm_rest.models.v0040_job_time_user import V0040JobTimeUser
from aind_slurm_rest.models.v0040_uint32_no_val import V0040Uint32NoVal
from typing import Optional, Set
from typing_extensions import Self

class V0040JobTime(BaseModel):
    """
    V0040JobTime
    """ # noqa: E501
    elapsed: Optional[StrictInt] = Field(default=None, description="Elapsed time in seconds")
    eligible: Optional[StrictInt] = Field(default=None, description="Time when the job became eligible to run (UNIX timestamp)")
    end: Optional[StrictInt] = Field(default=None, description="End time (UNIX timestamp)")
    start: Optional[StrictInt] = Field(default=None, description="Time execution began (UNIX timestamp)")
    submission: Optional[StrictInt] = Field(default=None, description="Time when the job was submitted (UNIX timestamp)")
    suspended: Optional[StrictInt] = Field(default=None, description="Total time in suspended state in seconds")
    system: Optional[V0040JobTimeSystem] = None
    limit: Optional[V0040Uint32NoVal] = None
    total: Optional[V0040JobTimeTotal] = None
    user: Optional[V0040JobTimeUser] = None
    __properties: ClassVar[List[str]] = ["elapsed", "eligible", "end", "start", "submission", "suspended", "system", "limit", "total", "user"]

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
        """Create an instance of V0040JobTime from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of system
        if self.system:
            _dict['system'] = self.system.to_dict()
        # override the default output from pydantic by calling `to_dict()` of limit
        if self.limit:
            _dict['limit'] = self.limit.to_dict()
        # override the default output from pydantic by calling `to_dict()` of total
        if self.total:
            _dict['total'] = self.total.to_dict()
        # override the default output from pydantic by calling `to_dict()` of user
        if self.user:
            _dict['user'] = self.user.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of V0040JobTime from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "elapsed": obj.get("elapsed"),
            "eligible": obj.get("eligible"),
            "end": obj.get("end"),
            "start": obj.get("start"),
            "submission": obj.get("submission"),
            "suspended": obj.get("suspended"),
            "system": V0040JobTimeSystem.from_dict(obj["system"]) if obj.get("system") is not None else None,
            "limit": V0040Uint32NoVal.from_dict(obj["limit"]) if obj.get("limit") is not None else None,
            "total": V0040JobTimeTotal.from_dict(obj["total"]) if obj.get("total") is not None else None,
            "user": V0040JobTimeUser.from_dict(obj["user"]) if obj.get("user") is not None else None
        })
        return _obj


