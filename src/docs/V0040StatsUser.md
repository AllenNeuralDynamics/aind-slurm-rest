# V0040StatsUser


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user** | **str** | User ID | [optional] 
**count** | **int** | Number of RPCs processed | [optional] 
**time** | [**SlurmdbV0041GetDiag200ResponseStatisticsRPCsInnerTime**](SlurmdbV0041GetDiag200ResponseStatisticsRPCsInnerTime.md) |  | [optional] 

## Example

```python
from aind_slurm_rest.models.v0040_stats_user import V0040StatsUser

# TODO update the JSON string below
json = "{}"
# create an instance of V0040StatsUser from a JSON string
v0040_stats_user_instance = V0040StatsUser.from_json(json)
# print the JSON string representation of the object
print V0040StatsUser.to_json()

# convert the object into a dict
v0040_stats_user_dict = v0040_stats_user_instance.to_dict()
# create an instance of V0040StatsUser from a dict
v0040_stats_user_form_dict = v0040_stats_user.from_dict(v0040_stats_user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


