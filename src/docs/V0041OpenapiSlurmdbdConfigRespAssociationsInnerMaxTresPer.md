# V0041OpenapiSlurmdbdConfigRespAssociationsInnerMaxTresPer


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**job** | [**List[SlurmdbV0041PostUsersAssociationRequestAssociationConditionAssociationGrptresInner]**](SlurmdbV0041PostUsersAssociationRequestAssociationConditionAssociationGrptresInner.md) | MaxTRESPerJob | [optional] 
**node** | [**List[SlurmdbV0041PostUsersAssociationRequestAssociationConditionAssociationGrptresInner]**](SlurmdbV0041PostUsersAssociationRequestAssociationConditionAssociationGrptresInner.md) | MaxTRESPerNode | [optional] 

## Example

```python
from aind_slurm_rest.models.v0041_openapi_slurmdbd_config_resp_associations_inner_max_tres_per import V0041OpenapiSlurmdbdConfigRespAssociationsInnerMaxTresPer

# TODO update the JSON string below
json = "{}"
# create an instance of V0041OpenapiSlurmdbdConfigRespAssociationsInnerMaxTresPer from a JSON string
v0041_openapi_slurmdbd_config_resp_associations_inner_max_tres_per_instance = V0041OpenapiSlurmdbdConfigRespAssociationsInnerMaxTresPer.from_json(json)
# print the JSON string representation of the object
print V0041OpenapiSlurmdbdConfigRespAssociationsInnerMaxTresPer.to_json()

# convert the object into a dict
v0041_openapi_slurmdbd_config_resp_associations_inner_max_tres_per_dict = v0041_openapi_slurmdbd_config_resp_associations_inner_max_tres_per_instance.to_dict()
# create an instance of V0041OpenapiSlurmdbdConfigRespAssociationsInnerMaxTresPer from a dict
v0041_openapi_slurmdbd_config_resp_associations_inner_max_tres_per_form_dict = v0041_openapi_slurmdbd_config_resp_associations_inner_max_tres_per.from_dict(v0041_openapi_slurmdbd_config_resp_associations_inner_max_tres_per_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


