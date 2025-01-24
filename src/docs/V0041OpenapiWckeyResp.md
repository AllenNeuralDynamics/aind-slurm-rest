# V0041OpenapiWckeyResp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**wckeys** | [**List[V0041OpenapiSlurmdbdConfigRespUsersInnerWckeysInner]**](V0041OpenapiSlurmdbdConfigRespUsersInnerWckeysInner.md) | wckeys | 
**meta** | [**SlurmV0041GetShares200ResponseMeta**](SlurmV0041GetShares200ResponseMeta.md) |  | [optional] 
**errors** | [**List[SlurmV0041GetShares200ResponseErrorsInner]**](SlurmV0041GetShares200ResponseErrorsInner.md) | Query errors | [optional] 
**warnings** | [**List[SlurmV0041GetShares200ResponseWarningsInner]**](SlurmV0041GetShares200ResponseWarningsInner.md) | Query warnings | [optional] 

## Example

```python
from aind_slurm_rest.models.v0041_openapi_wckey_resp import V0041OpenapiWckeyResp

# TODO update the JSON string below
json = "{}"
# create an instance of V0041OpenapiWckeyResp from a JSON string
v0041_openapi_wckey_resp_instance = V0041OpenapiWckeyResp.from_json(json)
# print the JSON string representation of the object
print V0041OpenapiWckeyResp.to_json()

# convert the object into a dict
v0041_openapi_wckey_resp_dict = v0041_openapi_wckey_resp_instance.to_dict()
# create an instance of V0041OpenapiWckeyResp from a dict
v0041_openapi_wckey_resp_form_dict = v0041_openapi_wckey_resp.from_dict(v0041_openapi_wckey_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


