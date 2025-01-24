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

from pydantic import BaseModel, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from aind_slurm_rest.models.slurm_v0041_get_shares200_response_meta_client import SlurmV0041GetShares200ResponseMetaClient
from aind_slurm_rest.models.slurm_v0041_get_shares200_response_meta_plugin import SlurmV0041GetShares200ResponseMetaPlugin
from aind_slurm_rest.models.slurm_v0041_get_shares200_response_meta_slurm import SlurmV0041GetShares200ResponseMetaSlurm
from typing import Optional, Set
from typing_extensions import Self

class SlurmV0041GetShares200ResponseMeta(BaseModel):
    """
    Slurm meta values
    """ # noqa: E501
    plugin: Optional[SlurmV0041GetShares200ResponseMetaPlugin] = None
    client: Optional[SlurmV0041GetShares200ResponseMetaClient] = None
    command: Optional[List[StrictStr]] = Field(default=None, description="CLI command (if applicable)")
    slurm: Optional[SlurmV0041GetShares200ResponseMetaSlurm] = None
    __properties: ClassVar[List[str]] = ["plugin", "client", "command", "slurm"]

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
        """Create an instance of SlurmV0041GetShares200ResponseMeta from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of plugin
        if self.plugin:
            _dict['plugin'] = self.plugin.to_dict()
        # override the default output from pydantic by calling `to_dict()` of client
        if self.client:
            _dict['client'] = self.client.to_dict()
        # override the default output from pydantic by calling `to_dict()` of slurm
        if self.slurm:
            _dict['slurm'] = self.slurm.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of SlurmV0041GetShares200ResponseMeta from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "plugin": SlurmV0041GetShares200ResponseMetaPlugin.from_dict(obj["plugin"]) if obj.get("plugin") is not None else None,
            "client": SlurmV0041GetShares200ResponseMetaClient.from_dict(obj["client"]) if obj.get("client") is not None else None,
            "command": obj.get("command"),
            "slurm": SlurmV0041GetShares200ResponseMetaSlurm.from_dict(obj["slurm"]) if obj.get("slurm") is not None else None
        })
        return _obj


