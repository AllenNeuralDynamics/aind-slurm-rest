# SlurmV0041GetShares200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**shares** | [**SlurmV0041GetShares200ResponseShares**](SlurmV0041GetShares200ResponseShares.md) |  | 
**meta** | [**SlurmV0041GetShares200ResponseMeta**](SlurmV0041GetShares200ResponseMeta.md) |  | [optional] 
**errors** | [**List[SlurmV0041GetShares200ResponseErrorsInner]**](SlurmV0041GetShares200ResponseErrorsInner.md) | Query errors | [optional] 
**warnings** | [**List[SlurmV0041GetShares200ResponseWarningsInner]**](SlurmV0041GetShares200ResponseWarningsInner.md) | Query warnings | [optional] 

## Example

```python
from aind_slurm_rest.models.slurm_v0041_get_shares200_response import SlurmV0041GetShares200Response

# TODO update the JSON string below
json = "{}"
# create an instance of SlurmV0041GetShares200Response from a JSON string
slurm_v0041_get_shares200_response_instance = SlurmV0041GetShares200Response.from_json(json)
# print the JSON string representation of the object
print SlurmV0041GetShares200Response.to_json()

# convert the object into a dict
slurm_v0041_get_shares200_response_dict = slurm_v0041_get_shares200_response_instance.to_dict()
# create an instance of SlurmV0041GetShares200Response from a dict
slurm_v0041_get_shares200_response_form_dict = slurm_v0041_get_shares200_response.from_dict(slurm_v0041_get_shares200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


