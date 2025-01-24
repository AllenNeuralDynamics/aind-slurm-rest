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

from pydantic import BaseModel, Field
from typing import Any, ClassVar, Dict, List, Optional
from aind_slurm_rest.models.slurmdb_v0041_post_users_association_request_association_condition_association_grptres_inner import SlurmdbV0041PostUsersAssociationRequestAssociationConditionAssociationGrptresInner
from typing import Optional, Set
from typing_extensions import Self

class V0041OpenapiSlurmdbdConfigRespQosInnerLimitsMaxTresPer(BaseModel):
    """
    V0041OpenapiSlurmdbdConfigRespQosInnerLimitsMaxTresPer
    """ # noqa: E501
    account: Optional[List[SlurmdbV0041PostUsersAssociationRequestAssociationConditionAssociationGrptresInner]] = Field(default=None, description="MaxTRESPerAccount")
    job: Optional[List[SlurmdbV0041PostUsersAssociationRequestAssociationConditionAssociationGrptresInner]] = Field(default=None, description="MaxTRESPerJob")
    node: Optional[List[SlurmdbV0041PostUsersAssociationRequestAssociationConditionAssociationGrptresInner]] = Field(default=None, description="MaxTRESPerNode")
    user: Optional[List[SlurmdbV0041PostUsersAssociationRequestAssociationConditionAssociationGrptresInner]] = Field(default=None, description="MaxTRESPerUser")
    __properties: ClassVar[List[str]] = ["account", "job", "node", "user"]

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
        """Create an instance of V0041OpenapiSlurmdbdConfigRespQosInnerLimitsMaxTresPer from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in account (list)
        _items = []
        if self.account:
            for _item in self.account:
                if _item:
                    _items.append(_item.to_dict())
            _dict['account'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in job (list)
        _items = []
        if self.job:
            for _item in self.job:
                if _item:
                    _items.append(_item.to_dict())
            _dict['job'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in node (list)
        _items = []
        if self.node:
            for _item in self.node:
                if _item:
                    _items.append(_item.to_dict())
            _dict['node'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in user (list)
        _items = []
        if self.user:
            for _item in self.user:
                if _item:
                    _items.append(_item.to_dict())
            _dict['user'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of V0041OpenapiSlurmdbdConfigRespQosInnerLimitsMaxTresPer from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "account": [SlurmdbV0041PostUsersAssociationRequestAssociationConditionAssociationGrptresInner.from_dict(_item) for _item in obj["account"]] if obj.get("account") is not None else None,
            "job": [SlurmdbV0041PostUsersAssociationRequestAssociationConditionAssociationGrptresInner.from_dict(_item) for _item in obj["job"]] if obj.get("job") is not None else None,
            "node": [SlurmdbV0041PostUsersAssociationRequestAssociationConditionAssociationGrptresInner.from_dict(_item) for _item in obj["node"]] if obj.get("node") is not None else None,
            "user": [SlurmdbV0041PostUsersAssociationRequestAssociationConditionAssociationGrptresInner.from_dict(_item) for _item in obj["user"]] if obj.get("user") is not None else None
        })
        return _obj


