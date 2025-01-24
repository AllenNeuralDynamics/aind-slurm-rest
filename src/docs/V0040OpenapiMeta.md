# V0040OpenapiMeta


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**plugin** | [**SlurmV0041GetShares200ResponseMetaPlugin**](SlurmV0041GetShares200ResponseMetaPlugin.md) |  | [optional] 
**client** | [**SlurmV0041GetShares200ResponseMetaClient**](SlurmV0041GetShares200ResponseMetaClient.md) |  | [optional] 
**command** | **List[str]** |  | [optional] 
**slurm** | [**SlurmV0041GetShares200ResponseMetaSlurm**](SlurmV0041GetShares200ResponseMetaSlurm.md) |  | [optional] 

## Example

```python
from aind_slurm_rest.models.v0040_openapi_meta import V0040OpenapiMeta

# TODO update the JSON string below
json = "{}"
# create an instance of V0040OpenapiMeta from a JSON string
v0040_openapi_meta_instance = V0040OpenapiMeta.from_json(json)
# print the JSON string representation of the object
print V0040OpenapiMeta.to_json()

# convert the object into a dict
v0040_openapi_meta_dict = v0040_openapi_meta_instance.to_dict()
# create an instance of V0040OpenapiMeta from a dict
v0040_openapi_meta_form_dict = v0040_openapi_meta.from_dict(v0040_openapi_meta_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


