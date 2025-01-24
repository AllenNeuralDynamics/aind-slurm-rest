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

from pydantic import BaseModel
from typing import Any, ClassVar, Dict, List, Optional
from aind_slurm_rest.models.v0041_openapi_slurmdbd_config_resp_qos_inner_limits_max_wall_clock_per_qos import V0041OpenapiSlurmdbdConfigRespQosInnerLimitsMaxWallClockPerQos
from typing import Optional, Set
from typing_extensions import Self

class V0041OpenapiSlurmdbdConfigRespAssociationsInnerMaxPerAccount(BaseModel):
    """
    V0041OpenapiSlurmdbdConfigRespAssociationsInnerMaxPerAccount
    """ # noqa: E501
    wall_clock: Optional[V0041OpenapiSlurmdbdConfigRespQosInnerLimitsMaxWallClockPerQos] = None
    __properties: ClassVar[List[str]] = ["wall_clock"]

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
        """Create an instance of V0041OpenapiSlurmdbdConfigRespAssociationsInnerMaxPerAccount from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of wall_clock
        if self.wall_clock:
            _dict['wall_clock'] = self.wall_clock.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of V0041OpenapiSlurmdbdConfigRespAssociationsInnerMaxPerAccount from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "wall_clock": V0041OpenapiSlurmdbdConfigRespQosInnerLimitsMaxWallClockPerQos.from_dict(obj["wall_clock"]) if obj.get("wall_clock") is not None else None
        })
        return _obj


