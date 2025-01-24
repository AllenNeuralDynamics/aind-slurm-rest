# V0040JobTimeUser


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**seconds** | **int** | User CPU time used by the job in seconds | [optional] 
**microseconds** | **int** | User CPU time used by the job in microseconds | [optional] 

## Example

```python
from aind_slurm_rest.models.v0040_job_time_user import V0040JobTimeUser

# TODO update the JSON string below
json = "{}"
# create an instance of V0040JobTimeUser from a JSON string
v0040_job_time_user_instance = V0040JobTimeUser.from_json(json)
# print the JSON string representation of the object
print V0040JobTimeUser.to_json()

# convert the object into a dict
v0040_job_time_user_dict = v0040_job_time_user_instance.to_dict()
# create an instance of V0040JobTimeUser from a dict
v0040_job_time_user_form_dict = v0040_job_time_user.from_dict(v0040_job_time_user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


