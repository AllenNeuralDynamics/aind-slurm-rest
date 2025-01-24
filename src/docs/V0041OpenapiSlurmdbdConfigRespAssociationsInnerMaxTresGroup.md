# V0041OpenapiSlurmdbdConfigRespAssociationsInnerMaxTresGroup


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**minutes** | [**List[SlurmdbV0041PostUsersAssociationRequestAssociationConditionAssociationGrptresInner]**](SlurmdbV0041PostUsersAssociationRequestAssociationConditionAssociationGrptresInner.md) | GrpTRESMins | [optional] 
**active** | [**List[SlurmdbV0041PostUsersAssociationRequestAssociationConditionAssociationGrptresInner]**](SlurmdbV0041PostUsersAssociationRequestAssociationConditionAssociationGrptresInner.md) | GrpTRESRunMins | [optional] 

## Example

```python
from aind_slurm_rest.models.v0041_openapi_slurmdbd_config_resp_associations_inner_max_tres_group import V0041OpenapiSlurmdbdConfigRespAssociationsInnerMaxTresGroup

# TODO update the JSON string below
json = "{}"
# create an instance of V0041OpenapiSlurmdbdConfigRespAssociationsInnerMaxTresGroup from a JSON string
v0041_openapi_slurmdbd_config_resp_associations_inner_max_tres_group_instance = V0041OpenapiSlurmdbdConfigRespAssociationsInnerMaxTresGroup.from_json(json)
# print the JSON string representation of the object
print V0041OpenapiSlurmdbdConfigRespAssociationsInnerMaxTresGroup.to_json()

# convert the object into a dict
v0041_openapi_slurmdbd_config_resp_associations_inner_max_tres_group_dict = v0041_openapi_slurmdbd_config_resp_associations_inner_max_tres_group_instance.to_dict()
# create an instance of V0041OpenapiSlurmdbdConfigRespAssociationsInnerMaxTresGroup from a dict
v0041_openapi_slurmdbd_config_resp_associations_inner_max_tres_group_form_dict = v0041_openapi_slurmdbd_config_resp_associations_inner_max_tres_group.from_dict(v0041_openapi_slurmdbd_config_resp_associations_inner_max_tres_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


