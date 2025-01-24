# V0039PartitionInfoQos


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allowed** | **str** |  | [optional] 
**deny** | **str** |  | [optional] 
**assigned** | **str** |  | [optional] 

## Example

```python
from aind_slurm_rest.models.v0039_partition_info_qos import V0039PartitionInfoQos

# TODO update the JSON string below
json = "{}"
# create an instance of V0039PartitionInfoQos from a JSON string
v0039_partition_info_qos_instance = V0039PartitionInfoQos.from_json(json)
# print the JSON string representation of the object
print V0039PartitionInfoQos.to_json()

# convert the object into a dict
v0039_partition_info_qos_dict = v0039_partition_info_qos_instance.to_dict()
# create an instance of V0039PartitionInfoQos from a dict
v0039_partition_info_qos_form_dict = v0039_partition_info_qos.from_dict(v0039_partition_info_qos_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


