# V0039PartitionInfoPriority


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**job_factor** | **int** |  | [optional] 
**tier** | **int** |  | [optional] 

## Example

```python
from aind_slurm_rest.models.v0039_partition_info_priority import V0039PartitionInfoPriority

# TODO update the JSON string below
json = "{}"
# create an instance of V0039PartitionInfoPriority from a JSON string
v0039_partition_info_priority_instance = V0039PartitionInfoPriority.from_json(json)
# print the JSON string representation of the object
print V0039PartitionInfoPriority.to_json()

# convert the object into a dict
v0039_partition_info_priority_dict = v0039_partition_info_priority_instance.to_dict()
# create an instance of V0039PartitionInfoPriority from a dict
v0039_partition_info_priority_form_dict = v0039_partition_info_priority.from_dict(v0039_partition_info_priority_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


