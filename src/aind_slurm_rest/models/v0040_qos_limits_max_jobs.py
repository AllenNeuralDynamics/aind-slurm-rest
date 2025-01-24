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
from aind_slurm_rest.models.v0040_qos_limits_max_jobs_active_jobs import V0040QosLimitsMaxJobsActiveJobs
from aind_slurm_rest.models.v0040_qos_limits_max_jobs_active_jobs_per import V0040QosLimitsMaxJobsActiveJobsPer
from typing import Optional, Set
from typing_extensions import Self

class V0040QosLimitsMaxJobs(BaseModel):
    """
    V0040QosLimitsMaxJobs
    """ # noqa: E501
    active_jobs: Optional[V0040QosLimitsMaxJobsActiveJobs] = None
    per: Optional[V0040QosLimitsMaxJobsActiveJobsPer] = None
    __properties: ClassVar[List[str]] = ["active_jobs", "per"]

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
        """Create an instance of V0040QosLimitsMaxJobs from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of active_jobs
        if self.active_jobs:
            _dict['active_jobs'] = self.active_jobs.to_dict()
        # override the default output from pydantic by calling `to_dict()` of per
        if self.per:
            _dict['per'] = self.per.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of V0040QosLimitsMaxJobs from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "active_jobs": V0040QosLimitsMaxJobsActiveJobs.from_dict(obj["active_jobs"]) if obj.get("active_jobs") is not None else None,
            "per": V0040QosLimitsMaxJobsActiveJobsPer.from_dict(obj["per"]) if obj.get("per") is not None else None
        })
        return _obj


