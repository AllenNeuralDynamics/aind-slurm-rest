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
from aind_slurm_rest.models.v0039_account import V0039Account
from aind_slurm_rest.models.v0039_assoc import V0039Assoc
from aind_slurm_rest.models.v0039_cluster_rec import V0039ClusterRec
from aind_slurm_rest.models.v0039_qos import V0039Qos
from aind_slurm_rest.models.v0039_tres import V0039Tres
from aind_slurm_rest.models.v0039_user import V0039User
from aind_slurm_rest.models.v0039_wckey import V0039Wckey
from typing import Optional, Set
from typing_extensions import Self

class Dbv0039SetConfig(BaseModel):
    """
    Dbv0039SetConfig
    """ # noqa: E501
    clusters: Optional[List[V0039ClusterRec]] = None
    tres: Optional[List[List[V0039Tres]]] = Field(default=None, alias="TRES")
    accounts: Optional[List[V0039Account]] = None
    users: Optional[List[V0039User]] = None
    qos: Optional[List[V0039Qos]] = None
    wckeys: Optional[List[V0039Wckey]] = None
    associations: Optional[List[V0039Assoc]] = None
    __properties: ClassVar[List[str]] = ["clusters", "TRES", "accounts", "users", "qos", "wckeys", "associations"]

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
        """Create an instance of Dbv0039SetConfig from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in clusters (list)
        _items = []
        if self.clusters:
            for _item in self.clusters:
                if _item:
                    _items.append(_item.to_dict())
            _dict['clusters'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in tres (list of list)
        _items = []
        if self.tres:
            for _item in self.tres:
                if _item:
                    _items.append(
                         [_inner_item.to_dict() for _inner_item in _item if _inner_item is not None]
                    )
            _dict['TRES'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in accounts (list)
        _items = []
        if self.accounts:
            for _item in self.accounts:
                if _item:
                    _items.append(_item.to_dict())
            _dict['accounts'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in users (list)
        _items = []
        if self.users:
            for _item in self.users:
                if _item:
                    _items.append(_item.to_dict())
            _dict['users'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in qos (list)
        _items = []
        if self.qos:
            for _item in self.qos:
                if _item:
                    _items.append(_item.to_dict())
            _dict['qos'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in wckeys (list)
        _items = []
        if self.wckeys:
            for _item in self.wckeys:
                if _item:
                    _items.append(_item.to_dict())
            _dict['wckeys'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in associations (list)
        _items = []
        if self.associations:
            for _item in self.associations:
                if _item:
                    _items.append(_item.to_dict())
            _dict['associations'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Dbv0039SetConfig from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "clusters": [V0039ClusterRec.from_dict(_item) for _item in obj["clusters"]] if obj.get("clusters") is not None else None,
            "TRES": [
                    [V0039Tres.from_dict(_inner_item) for _inner_item in _item]
                    for _item in obj["TRES"]
                ] if obj.get("TRES") is not None else None,
            "accounts": [V0039Account.from_dict(_item) for _item in obj["accounts"]] if obj.get("accounts") is not None else None,
            "users": [V0039User.from_dict(_item) for _item in obj["users"]] if obj.get("users") is not None else None,
            "qos": [V0039Qos.from_dict(_item) for _item in obj["qos"]] if obj.get("qos") is not None else None,
            "wckeys": [V0039Wckey.from_dict(_item) for _item in obj["wckeys"]] if obj.get("wckeys") is not None else None,
            "associations": [V0039Assoc.from_dict(_item) for _item in obj["associations"]] if obj.get("associations") is not None else None
        })
        return _obj


