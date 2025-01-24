# V0040StatsRpc


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rpc** | **str** | RPC type | [optional] 
**count** | **int** | Number of RPCs processed | [optional] 
**time** | [**SlurmdbV0041GetDiag200ResponseStatisticsRPCsInnerTime**](SlurmdbV0041GetDiag200ResponseStatisticsRPCsInnerTime.md) |  | [optional] 

## Example

```python
from aind_slurm_rest.models.v0040_stats_rpc import V0040StatsRpc

# TODO update the JSON string below
json = "{}"
# create an instance of V0040StatsRpc from a JSON string
v0040_stats_rpc_instance = V0040StatsRpc.from_json(json)
# print the JSON string representation of the object
print V0040StatsRpc.to_json()

# convert the object into a dict
v0040_stats_rpc_dict = v0040_stats_rpc_instance.to_dict()
# create an instance of V0040StatsRpc from a dict
v0040_stats_rpc_form_dict = v0040_stats_rpc.from_dict(v0040_stats_rpc_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


