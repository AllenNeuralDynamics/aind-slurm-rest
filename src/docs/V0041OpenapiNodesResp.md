# V0041OpenapiNodesResp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**nodes** | [**List[V0041OpenapiNodesRespNodesInner]**](V0041OpenapiNodesRespNodesInner.md) | List of nodes | 
**last_update** | [**V0041OpenapiNodesRespLastUpdate**](V0041OpenapiNodesRespLastUpdate.md) |  | 
**meta** | [**SlurmV0041GetShares200ResponseMeta**](SlurmV0041GetShares200ResponseMeta.md) |  | [optional] 
**errors** | [**List[SlurmV0041GetShares200ResponseErrorsInner]**](SlurmV0041GetShares200ResponseErrorsInner.md) | Query errors | [optional] 
**warnings** | [**List[SlurmV0041GetShares200ResponseWarningsInner]**](SlurmV0041GetShares200ResponseWarningsInner.md) | Query warnings | [optional] 

## Example

```python
from aind_slurm_rest.models.v0041_openapi_nodes_resp import V0041OpenapiNodesResp

# TODO update the JSON string below
json = "{}"
# create an instance of V0041OpenapiNodesResp from a JSON string
v0041_openapi_nodes_resp_instance = V0041OpenapiNodesResp.from_json(json)
# print the JSON string representation of the object
print V0041OpenapiNodesResp.to_json()

# convert the object into a dict
v0041_openapi_nodes_resp_dict = v0041_openapi_nodes_resp_instance.to_dict()
# create an instance of V0041OpenapiNodesResp from a dict
v0041_openapi_nodes_resp_form_dict = v0041_openapi_nodes_resp.from_dict(v0041_openapi_nodes_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


