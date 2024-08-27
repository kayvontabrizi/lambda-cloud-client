# coding: utf-8

"""
    Lambda Cloud API

    API for interacting with the Lambda GPU Cloud

    The version of the OpenAPI document: 1.5.3
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List
from lambda_cloud_client.models.instance_type import InstanceType
from lambda_cloud_client.models.region import Region
from typing import Optional, Set
from typing_extensions import Self


class InstanceTypes200ResponseDataValue(BaseModel):
    """
    InstanceTypes200ResponseDataValue
    """  # noqa: E501

    instance_type: InstanceType
    regions_with_capacity_available: List[Region] = Field(
        description="List of regions, if any, that have this instance type available"
    )
    __properties: ClassVar[List[str]] = [
        "instance_type",
        "regions_with_capacity_available",
    ]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of InstanceTypes200ResponseDataValue from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of instance_type
        if self.instance_type:
            _dict["instance_type"] = self.instance_type.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in regions_with_capacity_available (list)
        _items = []
        if self.regions_with_capacity_available:
            for (
                _item_regions_with_capacity_available
            ) in self.regions_with_capacity_available:
                if _item_regions_with_capacity_available:
                    _items.append(_item_regions_with_capacity_available.to_dict())
            _dict["regions_with_capacity_available"] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of InstanceTypes200ResponseDataValue from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "instance_type": InstanceType.from_dict(obj["instance_type"])
                if obj.get("instance_type") is not None
                else None,
                "regions_with_capacity_available": [
                    Region.from_dict(_item)
                    for _item in obj["regions_with_capacity_available"]
                ]
                if obj.get("regions_with_capacity_available") is not None
                else None,
            }
        )
        return _obj
