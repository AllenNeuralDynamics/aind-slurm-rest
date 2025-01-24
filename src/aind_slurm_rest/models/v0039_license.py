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

from pydantic import BaseModel, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class V0039License(BaseModel):
    """
    V0039License
    """ # noqa: E501
    license_name: Optional[StrictStr] = Field(default=None, alias="LicenseName")
    total: Optional[StrictInt] = Field(default=None, alias="Total")
    used: Optional[StrictInt] = Field(default=None, alias="Used")
    free: Optional[StrictInt] = Field(default=None, alias="Free")
    remote: Optional[StrictBool] = Field(default=None, alias="Remote")
    reserved: Optional[StrictInt] = Field(default=None, alias="Reserved")
    last_consumed: Optional[StrictInt] = Field(default=None, alias="LastConsumed")
    last_deficit: Optional[StrictInt] = Field(default=None, alias="LastDeficit")
    last_update: Optional[StrictInt] = Field(default=None, alias="LastUpdate")
    __properties: ClassVar[List[str]] = ["LicenseName", "Total", "Used", "Free", "Remote", "Reserved", "LastConsumed", "LastDeficit", "LastUpdate"]

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
        """Create an instance of V0039License from a JSON string"""
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
        """Create an instance of V0039License from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "LicenseName": obj.get("LicenseName"),
            "Total": obj.get("Total"),
            "Used": obj.get("Used"),
            "Free": obj.get("Free"),
            "Remote": obj.get("Remote"),
            "Reserved": obj.get("Reserved"),
            "LastConsumed": obj.get("LastConsumed"),
            "LastDeficit": obj.get("LastDeficit"),
            "LastUpdate": obj.get("LastUpdate")
        })
        return _obj


