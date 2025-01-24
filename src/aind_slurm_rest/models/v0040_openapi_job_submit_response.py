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
from aind_slurm_rest.models.v0040_job_submit_response_msg import V0040JobSubmitResponseMsg
from aind_slurm_rest.models.v0040_openapi_error import V0040OpenapiError
from aind_slurm_rest.models.v0040_openapi_meta import V0040OpenapiMeta
from aind_slurm_rest.models.v0040_openapi_warning import V0040OpenapiWarning
from typing import Optional, Set
from typing_extensions import Self

class V0040OpenapiJobSubmitResponse(BaseModel):
    """
    V0040OpenapiJobSubmitResponse
    """ # noqa: E501
    result: Optional[V0040JobSubmitResponseMsg] = None
    job_id: Optional[StrictInt] = Field(default=None, description="Submitted Job ID")
    step_id: Optional[StrictStr] = Field(default=None, description="Submitted Step ID")
    job_submit_user_msg: Optional[StrictStr] = Field(default=None, description="job submision user message")
    meta: Optional[V0040OpenapiMeta] = None
    errors: Optional[List[V0040OpenapiError]] = None
    warnings: Optional[List[V0040OpenapiWarning]] = None
    __properties: ClassVar[List[str]] = ["result", "job_id", "step_id", "job_submit_user_msg", "meta", "errors", "warnings"]

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
        """Create an instance of V0040OpenapiJobSubmitResponse from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of result
        if self.result:
            _dict['result'] = self.result.to_dict()
        # override the default output from pydantic by calling `to_dict()` of meta
        if self.meta:
            _dict['meta'] = self.meta.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in errors (list)
        _items = []
        if self.errors:
            for _item in self.errors:
                if _item:
                    _items.append(_item.to_dict())
            _dict['errors'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in warnings (list)
        _items = []
        if self.warnings:
            for _item in self.warnings:
                if _item:
                    _items.append(_item.to_dict())
            _dict['warnings'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of V0040OpenapiJobSubmitResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "result": V0040JobSubmitResponseMsg.from_dict(obj["result"]) if obj.get("result") is not None else None,
            "job_id": obj.get("job_id"),
            "step_id": obj.get("step_id"),
            "job_submit_user_msg": obj.get("job_submit_user_msg"),
            "meta": V0040OpenapiMeta.from_dict(obj["meta"]) if obj.get("meta") is not None else None,
            "errors": [V0040OpenapiError.from_dict(_item) for _item in obj["errors"]] if obj.get("errors") is not None else None,
            "warnings": [V0040OpenapiWarning.from_dict(_item) for _item in obj["warnings"]] if obj.get("warnings") is not None else None
        })
        return _obj


