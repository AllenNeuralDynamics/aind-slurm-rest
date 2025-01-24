# V0039ControllerPing


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hostname** | **str** |  | [optional] 
**pinged** | **str** |  | [optional] 
**latency** | **int** |  | [optional] 
**mode** | **str** |  | [optional] 

## Example

```python
from aind_slurm_rest.models.v0039_controller_ping import V0039ControllerPing

# TODO update the JSON string below
json = "{}"
# create an instance of V0039ControllerPing from a JSON string
v0039_controller_ping_instance = V0039ControllerPing.from_json(json)
# print the JSON string representation of the object
print V0039ControllerPing.to_json()

# convert the object into a dict
v0039_controller_ping_dict = v0039_controller_ping_instance.to_dict()
# create an instance of V0039ControllerPing from a dict
v0039_controller_ping_form_dict = v0039_controller_ping.from_dict(v0039_controller_ping_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


