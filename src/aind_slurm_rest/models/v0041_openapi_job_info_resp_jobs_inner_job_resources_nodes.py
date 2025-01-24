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
from aind_slurm_rest.models.v0041_openapi_job_info_resp_jobs_inner_job_resources_nodes_allocation_inner import V0041OpenapiJobInfoRespJobsInnerJobResourcesNodesAllocationInner
from typing import Optional, Set
from typing_extensions import Self

class V0041OpenapiJobInfoRespJobsInnerJobResourcesNodes(BaseModel):
    """
    V0041OpenapiJobInfoRespJobsInnerJobResourcesNodes
    """ # noqa: E501
    count: Optional[StrictInt] = Field(default=None, description="Number of allocated nodes")
    select_type: Optional[List[StrictStr]] = Field(default=None, description="Node scheduling selection method")
    list: Optional[StrictStr] = Field(default=None, description="Node(s) allocated to the job")
    whole: Optional[StrictBool] = Field(default=None, description="Whether whole nodes were allocated")
    allocation: Optional[List[V0041OpenapiJobInfoRespJobsInnerJobResourcesNodesAllocationInner]] = Field(default=None, description="Allocated node resources")
    __properties: ClassVar[List[str]] = ["count", "select_type", "list", "whole", "allocation"]

    @field_validator('select_type')
    def select_type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        for i in value:
            if i not in set(['AVAILABLE', 'ONE_ROW', 'RESERVED']):
                raise ValueError("each list item must be one of ('AVAILABLE', 'ONE_ROW', 'RESERVED')")
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
        """Create an instance of V0041OpenapiJobInfoRespJobsInnerJobResourcesNodes from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in allocation (list)
        _items = []
        if self.allocation:
            for _item in self.allocation:
                if _item:
                    _items.append(_item.to_dict())
            _dict['allocation'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of V0041OpenapiJobInfoRespJobsInnerJobResourcesNodes from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "count": obj.get("count"),
            "select_type": obj.get("select_type"),
            "list": obj.get("list"),
            "whole": obj.get("whole"),
            "allocation": [V0041OpenapiJobInfoRespJobsInnerJobResourcesNodesAllocationInner.from_dict(_item) for _item in obj["allocation"]] if obj.get("allocation") is not None else None
        })
        return _obj


