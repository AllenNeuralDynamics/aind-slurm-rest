# V0041OpenapiClustersResp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**clusters** | [**List[V0041OpenapiSlurmdbdConfigRespClustersInner]**](V0041OpenapiSlurmdbdConfigRespClustersInner.md) | clusters | 
**meta** | [**SlurmV0041GetShares200ResponseMeta**](SlurmV0041GetShares200ResponseMeta.md) |  | [optional] 
**errors** | [**List[SlurmV0041GetShares200ResponseErrorsInner]**](SlurmV0041GetShares200ResponseErrorsInner.md) | Query errors | [optional] 
**warnings** | [**List[SlurmV0041GetShares200ResponseWarningsInner]**](SlurmV0041GetShares200ResponseWarningsInner.md) | Query warnings | [optional] 

## Example

```python
from aind_slurm_rest.models.v0041_openapi_clusters_resp import V0041OpenapiClustersResp

# TODO update the JSON string below
json = "{}"
# create an instance of V0041OpenapiClustersResp from a JSON string
v0041_openapi_clusters_resp_instance = V0041OpenapiClustersResp.from_json(json)
# print the JSON string representation of the object
print V0041OpenapiClustersResp.to_json()

# convert the object into a dict
v0041_openapi_clusters_resp_dict = v0041_openapi_clusters_resp_instance.to_dict()
# create an instance of V0041OpenapiClustersResp from a dict
v0041_openapi_clusters_resp_form_dict = v0041_openapi_clusters_resp.from_dict(v0041_openapi_clusters_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


